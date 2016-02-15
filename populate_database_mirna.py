

def compare(first,second):
    if float(first[-2])>float(second[-2]):
        return 1
    elif float(first[-2])<float(second[-2]):
        return -1
    else:
        return 0


cancers=['BLCA','BRCA','CESC','COAD','ESCA','GBM','HNSC','KIRC','KIRP','LAML','LGG','LIHC','LUAD','LUSC','OV','PAAD',\
               'READ','SARC','SKCM','STAD','UCEC']

cancers=['BRCA','UCEC']
import numpy as np

f=open(r'C:\Users\Jordan Anaya\Desktop\omnesres\oncolnc\mirna\mature.fa')
transcript_to_names={i.split()[1]:i.split()[0].strip('>') for i in f if '>' in i}
names_to_transcripts={i:j for i,j in zip(transcript_to_names.values(),transcript_to_names.keys())}

for cancer in cancers:
    f=open(r'C:\Users\Jordan Anaya\Desktop\omnesres\oncolnc\mirna\cox'+'\\'+cancer+'\\'+'coeffs_pvalues_adjusted.txt')
    cox_results=[i.strip().split() for i in f]
    f=open(r'C:\Users\Jordan Anaya\Desktop\omnesres\oncolnc\mirna\cox'+'\\'+cancer+'\\'+'final_mirnas.txt')
    expression={}
    data=[eval(i.strip()) for i in f]
    for i in data:
        for j in i:
            expression[j[0]]=expression.get(j[0],[])+[j[1]]
    if cancer!='GBM':
        temp=[]
        for index,i in enumerate(sorted(cox_results,cmp=compare)):
            temp.append([i[0].upper(),names_to_transcripts[i[0]],round(float(i[1]),3),'%.2e' % float(i[2]),'%.2e' % float(i[3]),\
                         str(index+1),str(round(np.median(expression[i[0]]),2)),str(round(np.mean(expression[i[0]]),2)),\
                         str([round(k,2) for k in expression[i[0]]]),'miRNA'])
        w=open(r'C:\Users\Jordan Anaya\Desktop\omnesres\oncolnc\database'+'\\'+'mirna'+'\\'+cancer+'mirnadata.txt','w')
        for i in temp:
            w.write(str(i))
            w.write('\n')
        w.close()
    
            
    else:
        f2=open(r'C:\Users\Jordan Anaya\Desktop\omnesres\oncolnc\mirna\aliases.txt')
        aliases={}
        for i in f2:
            aliases[i.strip().split()[1]]=i.split()[0]
        names=[i[0] for i in cox_results]
        all_aliases={}
        for i in names:
            for j in aliases:
                    if i in j.split(';'):
                            all_aliases[i]=all_aliases.get(i,[])+[[j,aliases[j]]]
        temp=[]
        for index,i in enumerate(sorted(cox_results,cmp=compare)):
            if len(all_aliases[i[0]])==1:
                if all_aliases[i[0]][0][1] in transcript_to_names:
                    temp.append([transcript_to_names[all_aliases[i[0]][0][1]].upper(),all_aliases[i[0]][0][1],round(float(i[1]),3),'%.2e' % float(i[2]),'%.2e' % float(i[3]),\
                         str(index+1),str(round(np.median(expression[i[0]]),2)),str(round(np.mean(expression[i[0]]),2)),\
                         str([round(k,2) for k in expression[i[0]]]),'miRNA'])
        w=open(r'C:\Users\Jordan Anaya\Desktop\omnesres\oncolnc\database'+'\\'+'mirna'+'\\'+cancer+'mirnadata.txt','w')
        for i in temp:
            w.write(str(i))
            w.write('\n')
        w.close()


    del expression




