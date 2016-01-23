from django.db import models

# Create your models here.
class ALL_GENES(models.Model):
    gene=models.CharField(max_length=22)
    all_data=models.TextField(default="empty")

    def __unicode__(self):
        return self.gene
    
class ALL_GENE_IDS(models.Model):
    gene_id=models.CharField(max_length=22)
    all_data=models.TextField(default="empty")

    def __unicode__(self):
        return self.gene_id

class ONCOLNC(models.Model):
    cancer=models.CharField(max_length=4)
    gene=models.CharField(max_length=22)
    gene_id=models.CharField(max_length=12)
    Cox=models.CharField(max_length=6)
    p_value=models.CharField(max_length=7)
    fdr=models.CharField(max_length=7)
    rank=models.CharField(max_length=6)
    mean=models.CharField(max_length=6)
    median=models.CharField(max_length=6)
    expression=models.TextField(default="empty")
    species=models.CharField(max_length=6)

    def __unicode__(self):
        return self.gene




class mRNA_PATIENTS(models.Model):
    cancer=models.CharField(max_length=4)
    clinical=models.TextField(default="empty")

    def __unicode__(self):
        return self.cancer

class miRNA_PATIENTS(models.Model):
    cancer=models.CharField(max_length=4)
    clinical=models.TextField(default="empty")

    def __unicode__(self):
        return self.cancer

class lncRNA_PATIENTS(models.Model):
    cancer=models.CharField(max_length=4)
    clinical=models.TextField(default="empty")

    def __unicode__(self):
        return self.cancer
