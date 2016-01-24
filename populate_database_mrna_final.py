import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()

from pan_cancer.models import ONCOLNC_mRNA


from pan_cancer.models import mRNA_PATIENTS


cancers=['BLCA','BRCA','CESC','COAD','ESCA','GBM','HNSC','KIRC','KIRP','LAML','LGG','LIHC','LUAD','LUSC','OV','PAAD',\
               'READ','SARC','SKCM','STAD','UCEC']

f=open('for_oncolnc_mrna.txt')
for i in f:
    Gene=i.split('\t')[0].split('_')[0]
    Gene_id=i.split('\t')[0].split('_')[1]
    all_data=eval(i.split('\t')[1].strip())
    CANCERS=['']*21
    for k in all_data:
        if k['cancer']=='BLCA':
            CANCERS[0]=k
        elif k['cancer']=='BRCA':
            CANCERS[1]=k
        elif k['cancer']=='CESC':
            CANCERS[2]=k
        elif k['cancer']=='COAD':
            CANCERS[3]=k
        elif k['cancer']=='ESCA':
            CANCERS[4]=k
        elif k['cancer']=='GBM':
            CANCERS[5]=k
        elif k['cancer']=='HNSC':
            CANCERS[6]=k
        elif k['cancer']=='KIRC':
            CANCERS[7]=k
        elif k['cancer']=='KIRP':
            CANCERS[8]=k
        elif k['cancer']=='LAML':
            CANCERS[9]=k
        elif k['cancer']=='LGG':
            CANCERS[10]=k
        elif k['cancer']=='LIHC':
            CANCERS[11]=k
        elif k['cancer']=='LUAD':
            CANCERS[12]=k
        elif k['cancer']=='LUSC':
            CANCERS[13]=k
        elif k['cancer']=='OV':
            CANCERS[14]=k
        elif k['cancer']=='PAAD':
            CANCERS[15]=k
        elif k['cancer']=='READ':
            CANCERS[16]=k
        elif k['cancer']=='SARC':
            CANCERS[17]=k
        elif k['cancer']=='SKCM':
            CANCERS[18]=k
        elif k['cancer']=='STAD':
            CANCERS[19]=k
        elif k['cancer']=='UCEC':
            CANCERS[20]=k
        else:
            raise
    ONCOLNC_mRNA.objects.create(gene_id=Gene_id,gene=Gene,BLCA=CANCERS[0],BRCA=CANCERS[1],CESC=CANCERS[2],COAD=CANCERS[3],\
                             ESCA=CANCERS[4],GBM=CANCERS[5],HNSC=CANCERS[6],KIRC=CANCERS[7],KIRP=CANCERS[8],LAML=CANCERS[9],\
                             LGG=CANCERS[10],LIHC=CANCERS[11],LUAD=CANCERS[12],LUSC=CANCERS[13],OV=CANCERS[14],\
                             PAAD=CANCERS[15],READ=CANCERS[16],SARC=CANCERS[17],SKCM=CANCERS[18],STAD=CANCERS[19],UCEC=CANCERS[20])



for cancer in cancers:
    f=open(r'C:\Users\Jordan Anaya\Desktop\omnesres\oncolnc\mrna\cox'+'\\'+cancer+'\\'+'for_oncolnc.txt')
    mRNA_PATIENTS.objects.create(cancer=cancer,clinical=f.read())




