from django.contrib import admin
from .models import BLCA
from .models import BRCA
from .models import CESC
from .models import COAD
from .models import ESCA
from .models import GBM
from .models import HNSC
from .models import KIRC
from .models import KIRP
from .models import LAML
from .models import LGG
from .models import LIHC
from .models import LUAD
from .models import LUSC
from .models import OV
from .models import PAAD
from .models import READ
from .models import SARC
from .models import SKCM
from .models import STAD
from .models import UCEC
from .models import mRNA_PATIENTS
from .models import miRNA_PATIENTS
from .models import lncRNA_PATIENTS
# Register your models here.

admin.site.register(BLCA)
admin.site.register(BRCA)
admin.site.register(CESC)
admin.site.register(COAD)
admin.site.register(ESCA)
admin.site.register(GBM)
admin.site.register(HNSC)
admin.site.register(KIRC)
admin.site.register(KIRP)
admin.site.register(LAML)
admin.site.register(LGG)
admin.site.register(LIHC)
admin.site.register(LUAD)
admin.site.register(LUSC)
admin.site.register(OV)
admin.site.register(PAAD)
admin.site.register(READ)
admin.site.register(SARC)
admin.site.register(SKCM)
admin.site.register(STAD)
admin.site.register(UCEC)
admin.site.register(mRNA_PATIENTS)
admin.site.register(miRNA_PATIENTS)
admin.site.register(lncRNA_PATIENTS)
