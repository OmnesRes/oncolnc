import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()

from pan_cancer.models import ALL_GENES
from pan_cancer.models import ALL_GENE_IDS

from pan_cancer.models import ONCOLNC_miRNA

from pan_cancer.models import miRNA_PATIENTS

f=open('every_gene_sorted.txt')
data=[i.strip() for i in f]
ALL_GENES.objects.create(gene='all_genes',all_data=str(data))

f=open('every_gene_id_sorted.txt')
data=[i.strip() for i in f]
ALL_GENE_IDS.objects.create(gene_id='all_gene_ids',all_data=str(data))



cancers=['BLCA','BRCA','CESC','COAD','ESCA','GBM','HNSC','KIRC','KIRP','LAML','LGG','LIHC','LUAD','LUSC','OV','PAAD',\
               'READ','SARC','SKCM','STAD','UCEC']




for cancer in cancers:
    f=open(r'C:\Users\Jordan Anaya\Desktop\omnesres\oncolnc\database\mirna'+'\\'+cancer+'mirnadata.txt')
    data=[eval(i.strip()) for i in f]
    for j in data:
        ONCOLNC_miRNA.objects.create(cancer=cancer,gene=j[0],gene_id=j[1],Cox=str(j[2]),p_value=j[3],fdr=j[4],rank=j[5],mean=j[7],\
                                       median=j[6],expression=j[8])
 

for cancer in cancers:
    f=open(r'C:\Users\Jordan Anaya\Desktop\omnesres\oncolnc\mirna\cox'+'\\'+cancer+'\\'+'for_oncolnc.txt')
    miRNA_PATIENTS.objects.create(cancer=cancer,clinical=f.read())




