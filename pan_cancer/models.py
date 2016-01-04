from django.db import models

# Create your models here.

class BLCA(models.Model):
    gene=models.CharField(max_length=10)
    Cox=models.CharField(max_length=10)
    p_value=models.CharField(max_length=10)
    fdr=models.CharField(max_length=10)
    rank=models.CharField(max_length=10)
    expression=models.TextField(default="empty")

    def __unicode__(self):
        return self.gene

class BRCA(models.Model):
    gene=models.CharField(max_length=10)
    Cox=models.CharField(max_length=10)
    p_value=models.CharField(max_length=10)
    fdr=models.CharField(max_length=10)
    rank=models.CharField(max_length=10)
    expression=models.TextField(default="empty")

    def __unicode__(self):
        return self.gene

class CESC(models.Model):
    gene=models.CharField(max_length=10)
    Cox=models.CharField(max_length=10)
    p_value=models.CharField(max_length=10)
    fdr=models.CharField(max_length=10)
    rank=models.CharField(max_length=10)
    expression=models.TextField(default="empty")

    def __unicode__(self):
        return self.gene

class COAD(models.Model):
    gene=models.CharField(max_length=10)
    Cox=models.CharField(max_length=10)
    p_value=models.CharField(max_length=10)
    fdr=models.CharField(max_length=10)
    rank=models.CharField(max_length=10)
    expression=models.TextField(default="empty")

    def __unicode__(self):
        return self.gene

class GBM(models.Model):
    gene=models.CharField(max_length=10)
    Cox=models.CharField(max_length=10)
    p_value=models.CharField(max_length=10)
    fdr=models.CharField(max_length=10)
    rank=models.CharField(max_length=10)
    expression=models.TextField(default="empty")

    def __unicode__(self):
        return self.gene

class HNSC(models.Model):
    gene=models.CharField(max_length=10)
    Cox=models.CharField(max_length=10)
    p_value=models.CharField(max_length=10)
    fdr=models.CharField(max_length=10)
    rank=models.CharField(max_length=10)
    expression=models.TextField(default="empty")

    def __unicode__(self):
        return self.gene

class KIRC(models.Model):
    gene=models.CharField(max_length=10)
    Cox=models.CharField(max_length=10)
    p_value=models.CharField(max_length=10)
    fdr=models.CharField(max_length=10)
    rank=models.CharField(max_length=10)
    expression=models.TextField(default="empty")

    def __unicode__(self):
        return self.gene

class KIRP(models.Model):
    gene=models.CharField(max_length=10)
    Cox=models.CharField(max_length=10)
    p_value=models.CharField(max_length=10)
    fdr=models.CharField(max_length=10)
    rank=models.CharField(max_length=10)
    expression=models.TextField(default="empty")

    def __unicode__(self):
        return self.gene

class LAML(models.Model):
    gene=models.CharField(max_length=10)
    Cox=models.CharField(max_length=10)
    p_value=models.CharField(max_length=10)
    fdr=models.CharField(max_length=10)
    rank=models.CharField(max_length=10)
    expression=models.TextField(default="empty")

    def __unicode__(self):
        return self.gene

class LGG(models.Model):
    gene=models.CharField(max_length=10)
    Cox=models.CharField(max_length=10)
    p_value=models.CharField(max_length=10)
    fdr=models.CharField(max_length=10)
    rank=models.CharField(max_length=10)
    expression=models.TextField(default="empty")

    def __unicode__(self):
        return self.gene

class LIHC(models.Model):
    gene=models.CharField(max_length=10)
    Cox=models.CharField(max_length=10)
    p_value=models.CharField(max_length=10)
    fdr=models.CharField(max_length=10)
    rank=models.CharField(max_length=10)
    expression=models.TextField(default="empty")

    def __unicode__(self):
        return self.gene

class LUAD(models.Model):
    gene=models.CharField(max_length=10)
    Cox=models.CharField(max_length=10)
    p_value=models.CharField(max_length=10)
    fdr=models.CharField(max_length=10)
    rank=models.CharField(max_length=10)
    expression=models.TextField(default="empty")

    def __unicode__(self):
        return self.gene

class LUSC(models.Model):
    gene=models.CharField(max_length=10)
    Cox=models.CharField(max_length=10)
    p_value=models.CharField(max_length=10)
    fdr=models.CharField(max_length=10)
    rank=models.CharField(max_length=10)
    expression=models.TextField(default="empty")

    def __unicode__(self):
        return self.gene

class OV(models.Model):
    gene=models.CharField(max_length=10)
    Cox=models.CharField(max_length=10)
    p_value=models.CharField(max_length=10)
    fdr=models.CharField(max_length=10)
    rank=models.CharField(max_length=10)
    expression=models.TextField(default="empty")

    def __unicode__(self):
        return self.gene

class SKCM(models.Model):
    gene=models.CharField(max_length=10)
    Cox=models.CharField(max_length=10)
    p_value=models.CharField(max_length=10)
    fdr=models.CharField(max_length=10)
    rank=models.CharField(max_length=10)
    expression=models.TextField(default="empty")

    def __unicode__(self):
        return self.gene

class STAD(models.Model):
    gene=models.CharField(max_length=10)
    Cox=models.CharField(max_length=10)
    p_value=models.CharField(max_length=10)
    fdr=models.CharField(max_length=10)
    rank=models.CharField(max_length=10)
    expression=models.TextField(default="empty")

    def __unicode__(self):
        return self.gene

class PATIENTS(models.Model):
    cancer=models.CharField(max_length=10)
    clinical=models.TextField(default="empty")

    def __unicode__(self):
        return self.cancer
