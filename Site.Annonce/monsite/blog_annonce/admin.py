from django.contrib import admin

from .models import Annonce
from .models import Commentaire


admin.site.register(Annonce)
admin.site.register(Commentaire)