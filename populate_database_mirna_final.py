import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()

from pan_cancer.models import ALL_GENES
from pan_cancer.models import ALL_GENE_IDS

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

f=open(r'C:\Users\Jordan Anaya\Desktop\omnesres\oncolnc\database\every_gene.txt')
data=eval(f.read().strip())
for i in data:
    ALL_GENES.objects.create(gene=i.upper())

f=open(r'C:\Users\Jordan Anaya\Desktop\omnesres\oncolnc\database\every_gene_id.txt')
data=eval(f.read().strip())
for i in data:
    ALL_GENE_IDS.objects.create(gene_id=i.upper())


CANCERS={'BLCA':BLCA,'BRCA':BRCA,'CESC':CESC,'COAD':COAD,'ESCA':ESCA,'GBM':GBM,'HNSC':HNSC,'KIRC':KIRC,\
         'KIRP':KIRP,'LAML':LAML,'LGG':LGG,'LIHC':LIHC,'LUAD':LUAD,'LUSC':LUSC,'OV':OV,'PAAD':PAAD,\
         'READ':READ,'SARC':SARC,'SKCM':SKCM,'STAD':STAD,'UCEC':UCEC}

cancers=['BLCA','BRCA','CESC','COAD','ESCA','GBM','HNSC','KIRC','KIRP','LAML','LGG','LIHC','LUAD','LUSC','OV','PAAD',\
               'READ','SARC','SKCM','STAD','UCEC']




for cancer in cancers:
    f=open(r'C:\Users\Jordan Anaya\Desktop\omnesres\oncolnc\database\mirna'+'\\'+cancer+'mirnadata.txt')
    data=[eval(i.strip()) for i in f]
    for j in data:
        CANCERS[cancer].objects.create(gene=j[0],gene_id=j[1],Cox=str(j[2]),p_value=j[3],fdr=j[4],rank=j[5],mean=j[7],\
                                       median=j[6],expression=j[8],species='miRNA')
 

for cancer in cancers:
    f=open(r'C:\Users\Jordan Anaya\Desktop\omnesres\oncolnc\mirna\cox'+'\\'+cancer+'\\'+'for_oncolnc.txt')
    miRNA_PATIENTS.objects.create(cancer=cancer,clinical=f.read())




