import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()

from pan_cancer.models import ONCOLNC


from pan_cancer.models import mRNA_PATIENTS


cancers=['BLCA','BRCA','CESC','COAD','ESCA','GBM','HNSC','KIRC','KIRP','LAML','LGG','LIHC','LUAD','LUSC','OV','PAAD',\
               'READ','SARC','SKCM','STAD','UCEC']



for cancer in cancers:
    print cancer
    f=open(r'C:\Users\Jordan Anaya\Desktop\omnesres\oncolnc\database\mrna'+'\\'+cancer+'mrnadata.txt')
    data=[eval(i.strip()) for i in f]
    for j in data:
        ONCOLNC.objects.create(cancer=cancer,gene=j[0],gene_id=j[1],Cox=str(j[2]),p_value=j[3],fdr=j[4],rank=j[5],mean=j[7],\
                                       median=j[6],expression=j[8],species='mRNA')
 


for cancer in cancers:
    f=open(r'C:\Users\Jordan Anaya\Desktop\omnesres\oncolnc\mrna\cox'+'\\'+cancer+'\\'+'for_oncolnc.txt')
    mRNA_PATIENTS.objects.create(cancer=cancer,clinical=f.read())




