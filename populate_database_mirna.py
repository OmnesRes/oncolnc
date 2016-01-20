import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()

from pan_cancer.models import BLCA
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

from pan_cancer.models import miRNA_PATIENTS


def compare(first,second):
    if float(first[-2])>float(second[-2]):
        return 1
    elif float(first[-2])<float(second[-2]):
        return -1
    else:
        return 0





CANCERS={'BLCA':BLCA,'BRCA':BRCA,'CESC':CESC,'COAD':COAD,'ESCA':ESCA,'GBM':GBM,'HNSC':HNSC,'KIRC':KIRC,\
         'KIRP':KIRP,'LAML':LAML,'LGG':LGG,'LIHC':LIHC,'LUAD':LUAD,'LUSC':LUSC,'OV':OV,'PAAD':PAAD,\
         'READ':READ,'SARC':SARC,'SKCM':SKCM,'STAD':STAD,'UCEC':UCEC}

cancers=['BLCA','BRCA','CESC','COAD','ESCA','GBM','HNSC','KIRC','KIRP','LAML','LGG','LIHC','LUAD','LUSC','OV','PAAD',\
               'READ','SARC','SKCM','STAD','UCEC']

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
        for index,i in enumerate(sorted(cox_results,cmp=compare)):
            CANCERS[cancer].objects.create(gene=i[0].upper(),gene_id=names_to_transcripts[i[0]],Cox='%.2e' % float(i[1]),\
                                           p_value='%.2e' % float(i[2]),fdr='%.2e' % float(i[2]),rank=str(index+1),\
                                           mean=str(round(np.mean(expression[i[0]]),3)),median=str(round(np.median(expression[i[0]]),3)),\
                                           expression=str([round(k,3) for k in expression[i[0]]]),species='miRNA')
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
        for index,i in enumerate(sorted(cox_results,cmp=compare)):
            if len(all_aliases[i[0]])==1:
                if all_aliases[i[0]][0][1] in transcript_to_names:
                    CANCERS[cancer].objects.create(gene=transcript_to_names[all_aliases[i[0]][0][1]].upper(),gene_id=all_aliases[i[0]][0][1],Cox='%.2e' % float(i[1]),\
                                           p_value='%.2e' % float(i[2]),fdr='%.2e' % float(i[2]),rank=str(index+1),\
                                           mean=str(round(np.mean(expression[i[0]]),3)),median=str(round(np.median(expression[i[0]]),3)),\
                                           expression=str([round(k,3) for k in expression[i[0]]]),species='miRNA')


    del expression


for cancer in cancers:
    f=open(r'C:\Users\Jordan Anaya\Desktop\omnesres\oncolnc\mirna\cox'+'\\'+cancer+'\\'+'for_oncolnc.txt')
    miRNA_PATIENTS.objects.create(cancer=cancer,clinical=f.read())




