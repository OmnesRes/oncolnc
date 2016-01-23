from django.contrib import admin
from .models import ALL_GENES
from .models import ALL_GENE_IDS
from .models import ONCOLNC_mRNA
from .models import ONCOLNC_miRNA
from .models import ONCOLNC_lncRNA
from .models import mRNA_PATIENTS
from .models import miRNA_PATIENTS
from .models import lncRNA_PATIENTS
# Register your models here.

admin.site.register(ALL_GENES)
admin.site.register(ALL_GENE_IDS)
admin.site.register(ONCOLNC_mRNA)
admin.site.register(ONCOLNC_miRNA)
admin.site.register(ONCOLNC_lncRNA)
admin.site.register(mRNA_PATIENTS)
admin.site.register(miRNA_PATIENTS)
admin.site.register(lncRNA_PATIENTS)
