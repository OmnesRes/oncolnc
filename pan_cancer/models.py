from django.db import models

# Create your models here.

class BLCA(models.Model):
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

class BRCA(models.Model):
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

class CESC(models.Model):
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

class COAD(models.Model):
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

class ESCA(models.Model):
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

class GBM(models.Model):
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

class HNSC(models.Model):
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

class KIRC(models.Model):
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

class KIRP(models.Model):
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

class LAML(models.Model):
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

class LGG(models.Model):
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

class LIHC(models.Model):
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

class LUAD(models.Model):
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

class LUSC(models.Model):
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

class OV(models.Model):
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

class PAAD(models.Model):
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

class READ(models.Model):
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

class SARC(models.Model):
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


class SKCM(models.Model):
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

class STAD(models.Model):
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

class UCEC(models.Model):
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
