import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()

from pan_cancer.models import ALL_GENES
from pan_cancer.models import ALL_GENE_IDS

from pan_cancer.models import ONCOLNC_lncRNA
from pan_cancer.models import ONCOLNC_mRNA
from pan_cancer.models import ONCOLNC_miRNA

import time

for i in range(10):
    start=time.time()
##    result=ONCOLNC_lncRNA.objects.get(gene='A2M-AS1.1'.upper(),cancer='KIRC')
##    result=ONCOLNC_miRNA.objects.get(gene='hsa-miR-130b-3p'.upper(),cancer='KIRC')
##    result=ONCOLNC_mRNA.objects.get(gene='donson'.upper(),cancer='KIRC')
##    results=ONCOLNC_mRNA.objects.filter(gene='donson'.upper())
    results=ONCOLNC_miRNA.objects.filter(gene='hsa-miR-130b-3p'.upper())
    for result in results:
        result
    end=time.time()
    print end-start


