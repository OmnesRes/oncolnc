import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()

from pan_cancer.models import ONCOLNC

from pan_cancer.models import lncRNA_PATIENTS



cancers=['BLCA','BRCA','CESC','COAD','GBM','HNSC','KIRC','KIRP','LAML','LGG','LIHC','LUAD','LUSC','OV',\
               'READ','SKCM','STAD','UCEC']



for cancer in cancers:
    f=open(r'C:\Users\Jordan Anaya\Desktop\omnesres\oncolnc\database\lncrna'+'\\'+cancer+'lncrnadata.txt')
    data=[eval(i.strip()) for i in f]
    for j in data:
        ONCOLNC.objects.create(cancer=cancer,gene=j[0],gene_id=j[1],Cox=str(j[2]),p_value=j[3],fdr=j[4],rank=j[5],mean=j[7],\
                                       median=j[6],expression=j[8],species='lncRNA')
 

for cancer in cancers:
    f=open(r'C:\Users\Jordan Anaya\Desktop\omnesres\oncolnc\lncrna\cox'+'\\'+cancer+'\\'+'for_oncolnc.txt')
    lncRNA_PATIENTS.objects.create(cancer=cancer,clinical=f.read())




