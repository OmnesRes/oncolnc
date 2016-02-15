
def compare(first,second):
    if float(first[-2])>float(second[-2]):
        return 1
    elif float(first[-2])<float(second[-2]):
        return -1
    else:
        return 0

def myfunction(x):
	if x=='nan':
		return x
	else:
		return round(x,2)

conflicts={'UXT-AS1': 'T374161', 'CDKN2B-AS1': 'T356525', 'LINC00896': 'T229471', 'DCTN1-AS1': 'T192039', 'KCNQ1DN': 'T053312', 'INHBA-AS1': 'T322202', 'LINC00957': 'T322579', 'PACRG-AS1': 'T314859', 'LINC00310': 'T225427', 'LINC00938': 'T077318', 'LHFPL3-AS2': 'T330598', 'HAS2-AS1': 'T350375', 'TPT1-AS1': 'T093996', 'SPATA41': 'T123512', 'FAM13A-AS1': 'T268004', 'KCNQ1OT1': 'T053301', 'FLVCR1-AS1': 'T030165', 'ST7-AS1': 'T331729', 'FBXL19-AS1': 'T130509', 'TP53TG1': 'T327859', 'ZNF674-AS1': 'T373973', 'TMEM254-AS1': 'T044971', 'GLIS3-AS1': 'T355099', 'LINC00526': 'T158027', 'PSMG3-AS1': 'T317341', 'ZNF252P-AS1': 'T354539', 'LINC00323': 'T226507', 'IDI2-AS1': 'T035325', 'JHDM1D-AS1': 'T334335', 'PDCD4-AS1': 'T048595', 'BCDIN3D-AS1': 'T078256', 'MIR155HG': 'T224489', 'LINC01144': 'T010080', 'EMX2OS': 'T049262', 'LINC00606': 'T237949', 'LINC00092': 'T363122', 'FTX': 'T376410', 'USP27X-AS1': 'T374751', 'TMPO-AS1': 'T084753', 'LINC00494': 'T219315', 'LINC00094': 'T368432', 'LINC00654': 'T213242', 'TAPT1-AS1': 'T261843', 'PRAC2': 'T149878', 'KRTAP5-AS1': 'T052785', 'ILF3-AS1': 'T168322', 'LINC00599': 'T338703', 'JMJD1C-AS1': 'T042844', 'GNAS-AS1': 'T221110', 'LINC00174': 'T325600', 'DICER1-AS1': 'T109603', 'NEAT1': 'T061237', 'LINC01018': 'T278454', 'AFAP1-AS1': 'T260658', 'RPL34-AS1': 'T269318', 'LINC00114': 'T226069', 'HCG11': 'T299308', 'ADORA2A-AS1': 'T231001', 'LINC00261': 'T215042', 'MESTIT1': 'T333265', 'LINC00240': 'T299438', 'BDNF-AS': 'T056354', 'LINC01003': 'T336230', 'SNAI3-AS1': 'T138265', 'SNHG9': 'T125200', 'SOX2-OT': 'T255513'}



##cancers=['BLCA','BRCA','CESC','COAD','GBM','HNSC','KIRC','KIRP','LAML','LGG','LIHC','LUAD','LUSC','OV',\
##               'READ','SKCM','STAD','UCEC']

cancers=['BRCA','UCEC']
import numpy as np
f=open(r'C:\Users\Jordan Anaya\Desktop\omnesres\oncolnc\lncrna\mitranscriptome.gtf\mitranscriptome.gtf\mitranscriptome.v2.gtf\mitranscriptome.v2.gtf')
transcript_dict={}
for i in f:
    transcript_dict[i.split('transcript_id')[1].strip().split('";')[0].strip('"')]=i.strip().split()[-1].split('";')[0].strip('"')


for cancer in cancers:
    f=open(r'C:\Users\Jordan Anaya\Desktop\omnesres\oncolnc\lncrna\cox'+'\\'+cancer+'\\'+'coeffs_pvalues_adjusted.txt')
    cox_results=[i.strip().split() for i in f]
    f=open(r'C:\Users\Jordan Anaya\Desktop\omnesres\oncolnc\lncrna\cox'+'\\'+cancer+'\\'+'final_lncrnas.txt')
    expression={}
    data=[eval(i.strip().replace('nan',"'nan'")) for i in f]
    for i in data:
        for j in i:
            expression[j[0]]=expression.get(j[0],[])+[j[1]]
    temp=[]
    for index,i in enumerate(sorted(cox_results,cmp=compare)):
        if transcript_dict[i[0]] not in conflicts:
            temp.append([transcript_dict[i[0]].upper(),i[0],round(float(i[1]),3),'%.2e' % float(i[2]),'%.2e' % float(i[3]),\
                         str(index+1),str(round(np.median([float(k) for k in expression[i[0]]]),2)),\
                         str(round(np.mean([k for k in expression[i[0]] if k!='nan']),2)),\
                         str(map(myfunction,expression[i[0]])),'lncRNA'])
        else:
            temp.append(['',i[0],round(float(i[1]),3),'%.2e' % float(i[2]),'%.2e' % float(i[3]),\
                         str(index+1),str(round(np.median([float(k) for k in expression[i[0]]]),2)),\
                         str(round(np.mean([k for k in expression[i[0]] if k!='nan']),2)),\
                         str(map(myfunction,expression[i[0]])),'lncRNA'])
                        
    w=open(r'C:\Users\Jordan Anaya\Desktop\omnesres\oncolnc\database'+'\\'+'lncrna'+'\\'+cancer+'lncrnadata.txt','w')
    for i in temp:
        w.write(str(i))
        w.write('\n')
    w.close()
    del expression






