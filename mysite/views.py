from django.http import  Http404, HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
from pan_cancer.models import BLCA
from pan_cancer.models import BRCA
from pan_cancer.models import CESC
from pan_cancer.models import COAD
from pan_cancer.models import ESCA
from pan_cancer.models import GBM
from pan_cancer.models import HNSC
from pan_cancer.models import KIRC
from pan_cancer.models import KIRP
from pan_cancer.models import LAML
from pan_cancer.models import LGG
from pan_cancer.models import LIHC
from pan_cancer.models import LUAD
from pan_cancer.models import LUSC
from pan_cancer.models import OV
from pan_cancer.models import PAAD
from pan_cancer.models import READ
from pan_cancer.models import SARC
from pan_cancer.models import SKCM
from pan_cancer.models import STAD
from pan_cancer.models import UCEC
from pan_cancer.models import mRNA_PATIENTS
from pan_cancer.models import miRNA_PATIENTS
from pan_cancer.models import lncRNA_PATIENTS



cancers=['BLCA','BRCA','CESC','COAD','ESCA','GBM','HNSC','KIRC','KIRP','LAML','LGG','LIHC','LUAD','LUSC','OV',\
         'PAAD','READ','SARC','SKCM','STAD','UCEC']
CANCERS={'BLCA':BLCA,'BRCA':BRCA,'CESC':CESC,'COAD':COAD,'ESCA':ESCA,'GBM':GBM,'HNSC':HNSC,'KIRC':KIRC,'KIRP':KIRP,'LAML':LAML,\
         'LGG':LGG,'LIHC':LIHC,'LUAD':LUAD,'LUSC':LUSC,'OV':OV,'PAAD':PAAD,'READ':READ,'SARC':SARC,'SKCM':SKCM,'STAD':STAD,'UCEC':UCEC}
death_dic={"Alive":0,"Dead":1}



def plot_kaplan(survtimes):
    h_coords=[]
    v_coords=[]
    lost=[]
    y=1
    x=0
    for i in survtimes:
        if i[1]!='Dead':
            lost.append([i[0],y])
        else:
            h_coords.append([i[0],y])
            y=1*len(survtimes[survtimes.index(i)+1:])/float(len(survtimes[survtimes.index(i):]))
            v_coords.append([i[0],h_coords[-1][-1],y])
            break
    newsurv=survtimes[survtimes.index(i)+1:]
    while len(newsurv)>0:
        newsurv,y,h_coords,v_coords,lost=loop(newsurv,y,h_coords,v_coords,lost)
    return (h_coords,v_coords,lost)


def loop(newsurv,y,h_coords,v_coords,lost):
    for j in newsurv:
        if j[1]!='Dead':
            lost.append([j[0],y])
        else:
            h_coords.append([j[0],y])
            y=y*len(newsurv[newsurv.index(j)+1:])/float(len(newsurv[newsurv.index(j):]))
            v_coords.append([j[0],h_coords[-1][-1],y])
            break
    newsurv=newsurv[newsurv.index(j)+1:]
    return (newsurv,y,h_coords,v_coords,lost)


def home(request):
    return render(request, 'home.html')




def search_results(request):
    if request.META.get('HTTP_REFERER',False):
        error=False
        results=[]
        if 'q' in request.GET:
            raw=request.GET['q'].strip()
            if raw=='':
                return render(request, 'home.html', {'empty': True})
            q=request.GET['q'].strip().upper()
            for i in cancers:
                try:
                    gene=CANCERS[i].objects.get(gene=q)
                    results.append(gene)
                except:
                    results.append(None)
            if results==[None]*21:
                results=[]
                for i in cancers:
                    try:
                        gene=CANCERS[i].objects.get(gene_id=q)
                        results.append(gene)
                    except:
                        results.append(None)
                if results==[None]*21:
                    error=True
                    return render(request, 'home.html', {'error': error})
            missing=False
            if None in results:
                missing=True
            return render(request, 'search_results.html',
                          {'results':results, 'cancers': cancers,'missing':missing,'raw':raw})
        else:
            return render(request, 'home.html', {'error': error})
    else:
        return HttpResponse('Please get to this page by clicking the Submit button ;)')





def kaplan(request):
    import re
    from rpy2 import robjects as ro
    ro.r('library(survival)')
    cancer=request.GET.get('cancer','none')
    gene_id=request.GET.get('gene_id','none')
    lower=request.GET.get('lower',False)
    upper=request.GET.get('upper',False)
    raw=request.GET.get('raw','none')
    if request.META.get('HTTP_REFERER',False):
        if lower and upper:
            if not re.search('^[0-9]+$',lower) or not re.search('^[0-9]+$',upper):
                return render(request, 'kaplan.html', {'gene_id': gene_id,'cancer':cancer,'raw':raw,'lower':lower,'upper':upper,\
                                                       'addition_error':False,'input_error':True,'empty_error':False,\
                                                       'upper_error':False})
            elif int(lower)+int(upper)>100:
                return render(request, 'kaplan.html', {'gene_id': gene_id,'cancer':cancer,'raw':raw,'lower':lower, 'upper':upper,\
                                                       'addition_error':True,'input_error':False,'empty_error':False,\
                                                       'upper_error':False})
            elif int(upper)==100:
                return render(request, 'kaplan.html', {'gene_id': gene_id,'cancer':cancer,'raw':raw, 'lower':lower, 'upper':upper,\
                                                       'addition_error':False,'input_error':False,'empty_error':False,\
                                                       'upper_error':True})
            else:
                if CANCERS[cancer].objects.get(gene_id=gene_id).species=='mRNA':
                    patients=eval(mRNA_PATIENTS.objects.get(cancer=cancer).clinical)
                elif CANCERS[cancer].objects.get(gene_id=gene_id).species=='miRNA':
                    patients=eval(miRNA_PATIENTS.objects.get(cancer=cancer).clinical)
                else:
                    patients=eval(lncRNA_PATIENTS.objects.get(cancer=cancer).clinical)
                expression=eval(CANCERS[cancer].objects.get(gene_id=gene_id).expression)
                data=[[i,j] for i,j in zip(expression,patients) if i!='nan']
                data.sort()
                bottom=int(len(data)*int(lower)/100.0)
                top=int(len(data)*int(upper)/100.0)*-1
                bottom_patients=[i[1]+[(str(i[0])+'\n')] for i in data[:bottom]]
                if top==0:
                    top_patients=[]
                else:
                    top_patients=[i[1]+[(str(i[0])+'\n')] for i in data[top:]]
                first_line='{0:<16}{1:<5}{2:>10}{3:>15}'.format('Patient','Days','Status','Expression\n')
                low_patients=first_line+''.join(['{0:<15} {1:<5} {2:>9} {3:>14}'.format(i[0],str(i[1]),i[2],i[3]) for i in bottom_patients])
                high_patients=first_line+''.join(['{0:<15} {1:<5} {2:>9} {3:>14}'.format(i[0],str(i[1]),i[2],i[3]) for i in top_patients])
                if int(lower)!=100:
                    times=[i[1] for i in bottom_patients]+[i[1] for i in top_patients]
                    died=[death_dic[i[2]] for i in bottom_patients]+[death_dic[i[2]] for i in top_patients]
                    group=[1 for i in bottom_patients]+[2 for i in top_patients]
                    ro.globalenv['times']=ro.IntVector(times)
                    ro.globalenv['died']=ro.IntVector(died)
                    ro.globalenv['group']=ro.IntVector(group)
                    res=ro.r('survdiff(formula = Surv(times, died) ~ as.factor(group))')
                    logrank=str(res).split()[-1]
                else:
                    logrank=False
                return render(request, 'kaplan.html', {'gene_id':gene_id,'cancer':cancer,'raw':raw,'lower':lower,'upper':upper,'addition_error':False,\
                                                       'input_error':False,'empty_error':False,'low_patients':low_patients,\
                                                       'high_patients':high_patients,'upper_error':False,'logrank':logrank})
        elif (lower and not upper) or (upper and not lower):
            return render(request, 'kaplan.html', {'gene_id':gene_id,'cancer':cancer,'raw':raw,'lower':lower,'upper':upper,'addition_error':False,\
                                                       'input_error':False,'empty_error':True,'upper_error':False})
        else:
            return render(request, 'kaplan.html', {'gene_id':gene_id,'cancer':cancer,'raw':raw,'lower':lower,'upper':upper,'addition_error':False,\
                                                       'input_error':False,'empty_error':False,'upper_error':False})
    else:
        return HttpResponse('Please get to this page by clicking the PLOT button ;)')
   

def make_kaplan(request):
    from matplotlib.backends.backend_agg import FigureCanvasAgg
    from matplotlib.figure import Figure
    import matplotlib.pyplot as plt
    import gc
    message='Please get to this page by clicking the PLOT button ;)'
    if not request.META.get('HTTP_REFERER',False):
        return HttpResponse(message)
    else:
        Cancer=request.META['HTTP_REFERER'].split('cancer=')[1].split('&')[0]
        Gene_id=request.META['HTTP_REFERER'].split('gene_id=')[1].split('&')[0]
        Raw=request.META['HTTP_REFERER'].split('raw=')[1]
        Lower=request.META['HTTP_REFERER'].split('lower=')[1].split('&')[0]
        Upper=request.META['HTTP_REFERER'].split('upper=')[1].split('&')[0]
        if CANCERS[Cancer].objects.get(gene_id=Gene_id).species=='mRNA':
            patients=eval(mRNA_PATIENTS.objects.get(cancer=Cancer).clinical)
        elif CANCERS[Cancer].objects.get(gene_id=Gene_id).species=='miRNA':
            patients=eval(miRNA_PATIENTS.objects.get(cancer=Cancer).clinical)
        else:
            patients=eval(lncRNA_PATIENTS.objects.get(cancer=Cancer).clinical)
        expression=eval(CANCERS[Cancer].objects.get(gene_id=Gene_id).expression)
        data=[[i,j] for i,j in zip(expression,patients) if i!='nan']
        data.sort()
        bottom=int(len(data)*int(Lower)/100.0)
        top=int(len(data)*int(Upper)/100.0)*-1
        bottom_patients=[i[1] for i in data[:bottom]]
        if top==0:
            top_patients=[[]]
        else:
            top_patients=[i[1] for i in data[top:]]
        survtimes=[[int(i[1]),i[2]] for i in bottom_patients]
        survtimes.sort(key=lambda x:(x[0],x[1]))
        k_plot=plot_kaplan(survtimes)
        fig=Figure(figsize=(22.62372, 12),facecolor='white')
        ax=fig.add_subplot(111,)
        fig.subplots_adjust(bottom=.15)
        fig.subplots_adjust(top=1)
        width=3
        start=0
        for i in k_plot[0]:
            ax.hlines(i[1]*100,start,i[0],linewidths=width,color='b',label='cluster 1')
            start=i[0]

        if k_plot[-1][-1][0]>k_plot[0][-1][0]:
            ax.hlines(k_plot[-1][-1][1]*100,k_plot[0][-1][0],k_plot[-1][-1][0],linewidths=width,color='b')

        for i in k_plot[1]:
            cluster1=ax.vlines(i[0],i[2]*100-(width*715/10000.0),i[1]*100+(width*715/10000.0),linewidths=width,color='b')


        for i in k_plot[2]:
            ax.vlines(i[0],(i[1]-.01)*100,(i[1]+.01)*100,color='b')
        if top!=0:
            survtimes=[[int(i[1]),i[2]] for i in top_patients]
            survtimes.sort(key=lambda x:(x[0],x[1]))
            k_plot=plot_kaplan(survtimes)
            start=0
            for i in k_plot[0]:
                ax.hlines(i[1]*100,start,i[0],linewidths=width,color='r',label='cluster 2')
                start=i[0]

            if k_plot[-1][-1][0]>k_plot[0][-1][0]:
                ax.hlines(k_plot[-1][-1][1]*100,k_plot[0][-1][0],k_plot[-1][-1][0],linewidths=width,color='r')

            for i in k_plot[1]:
                cluster2=ax.vlines(i[0],i[2]*100-(width*715/10000.0),i[1]*100+(width*715/10000.0),linewidths=width,color='r')


            for i in k_plot[2]:
                ax.vlines(i[0],(i[1]-.01)*100,(i[1]+.01)*100,color='r')
        ax.tick_params(axis='x',length=15,width=3,direction='out',labelsize=30)
        ax.tick_params(axis='y',length=15,width=3,direction='out',labelsize=30)
        ax.spines['bottom'].set_position(['outward',10])
        ax.spines['left'].set_position(['outward',10])
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_linewidth(3)
        ax.spines['bottom'].set_linewidth(3)
        ax.spines['left'].set_bounds(0,100)
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        cluster1=ax.hlines(0,0,0,linewidths=10,color='b',label='cluster 1')
        if top!=0:
            cluster2=ax.hlines(0,0,0,linewidths=10,color='r',label='cluster 2')
        if top!=0:
            ax.legend((cluster1,cluster2),('   Low \n N=%s' % len(bottom_patients),'   High \n N=%s' % len(top_patients)),\
                      frameon=False,fontsize=25,ncol=2, loc='upper center',handletextpad=0,borderpad=0)
        else:
            pass
        ax.set_ylim(0,105)
        ax.set_xlim(0,)
        ax.set_xlabel('Days',fontsize=40,labelpad=20)
        ax.set_ylabel('% Surviving',fontsize=40)
        canvas=FigureCanvasAgg(fig)
        response=HttpResponse(content_type='image/png')
        canvas.print_png(response)
        fig.clf()
        plt.close(fig)
        del canvas
        gc.collect()
        return response

def download_kaplan(request):
    from matplotlib.backends.backend_agg import FigureCanvasAgg
    from matplotlib.figure import Figure
    import matplotlib.pyplot as plt
    import StringIO
    import gc
    message='Please get to this page by clicking the PLOT button ;)'
    if not request.META.get('HTTP_REFERER',False):
        return HttpResponse(message)
    else:
        Cancer=request.META['HTTP_REFERER'].split('cancer=')[1].split('&')[0]
        Gene_id=request.META['HTTP_REFERER'].split('gene_id=')[1].split('&')[0]
        Lower=request.META['HTTP_REFERER'].split('lower=')[1].split('&')[0]
        Upper=request.META['HTTP_REFERER'].split('upper=')[1].split('&')[0]
        if CANCERS[Cancer].objects.get(gene_id=Gene_id).species=='mRNA':
            patients=eval(mRNA_PATIENTS.objects.get(cancer=Cancer).clinical)
        elif CANCERS[Cancer].objects.get(gene_id=Gene_id).species=='miRNA':
            patients=eval(miRNA_PATIENTS.objects.get(cancer=Cancer).clinical)
        else:
            patients=eval(lncRNA_PATIENTS.objects.get(cancer=Cancer).clinical)
        expression=eval(CANCERS[Cancer].objects.get(gene_id=Gene_id).expression)
        data=[[i,j] for i,j in zip(expression,patients) if i!='nan']
        data.sort()
        bottom=int(len(data)*int(Lower)/100.0)
        top=int(len(data)*int(Upper)/100.0)*-1
        bottom_patients=[i[1] for i in data[:bottom]]
        if top==0:
            top_patients=[[]]
        else:
            top_patients=[i[1] for i in data[top:]]
        survtimes=[[int(i[1]),i[2]] for i in bottom_patients]
        survtimes.sort(key=lambda x:(x[0],x[1]))
        k_plot=plot_kaplan(survtimes)
        fig=Figure(figsize=(22.62372, 12),facecolor='white')
        ax=fig.add_subplot(111,)
        fig.subplots_adjust(bottom=.15)
        fig.subplots_adjust(top=1)
        width=3
        start=0
        for i in k_plot[0]:
            ax.hlines(i[1]*100,start,i[0],linewidths=width,color='b',label='cluster 1')
            start=i[0]

        if k_plot[-1][-1][0]>k_plot[0][-1][0]:
            ax.hlines(k_plot[-1][-1][1]*100,k_plot[0][-1][0],k_plot[-1][-1][0],linewidths=width,color='b')

        for i in k_plot[1]:
            cluster1=ax.vlines(i[0],i[2]*100-(width*715/10000.0),i[1]*100+(width*715/10000.0),linewidths=width,color='b')


        for i in k_plot[2]:
            ax.vlines(i[0],(i[1]-.01)*100,(i[1]+.01)*100,color='b')
        if top!=0:
            survtimes=[[int(i[1]),i[2]] for i in top_patients]
            survtimes.sort(key=lambda x:(x[0],x[1]))
            k_plot=plot_kaplan(survtimes)
            start=0
            for i in k_plot[0]:
                ax.hlines(i[1]*100,start,i[0],linewidths=width,color='r',label='cluster 2')
                start=i[0]

            if k_plot[-1][-1][0]>k_plot[0][-1][0]:
                ax.hlines(k_plot[-1][-1][1]*100,k_plot[0][-1][0],k_plot[-1][-1][0],linewidths=width,color='r')

            for i in k_plot[1]:
                cluster2=ax.vlines(i[0],i[2]*100-(width*715/10000.0),i[1]*100+(width*715/10000.0),linewidths=width,color='r')


            for i in k_plot[2]:
                ax.vlines(i[0],(i[1]-.01)*100,(i[1]+.01)*100,color='r')
        ax.tick_params(axis='x',length=15,width=3,direction='out',labelsize=30)
        ax.tick_params(axis='y',length=15,width=3,direction='out',labelsize=30)
        ax.spines['bottom'].set_position(['outward',10])
        ax.spines['left'].set_position(['outward',10])
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_linewidth(3)
        ax.spines['bottom'].set_linewidth(3)
        ax.spines['left'].set_bounds(0,100)
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        cluster1=ax.hlines(0,0,0,linewidths=10,color='b',label='cluster 1')
        if top!=0:
            cluster2=ax.hlines(0,0,0,linewidths=10,color='r',label='cluster 2')
        if top!=0:
            ax.legend((cluster1,cluster2),('   Low \n N=%s' % len(bottom_patients),'   High \n N=%s' % len(top_patients)),\
                      frameon=False,fontsize=25,ncol=2, loc='upper center',handletextpad=0,borderpad=0)
        else:
            pass
        ax.set_ylim(0,105)
        ax.set_xlim(0,)
        ax.set_xlabel('Days',fontsize=40,labelpad=20)
        ax.set_ylabel('% Surviving',fontsize=40)
        canvas=FigureCanvasAgg(fig)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename=%s_%s_%s_%s.pdf' % (Cancer,Gene_id,Lower,Upper)
        buffer=StringIO.StringIO()
        canvas.print_pdf(buffer)
        pdf=buffer.getvalue()
        buffer.close()
        response.write(pdf)
        fig.clf()
        plt.close(fig)
        del canvas
        gc.collect()
        return response

