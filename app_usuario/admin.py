from django.contrib import admin
from .models import UsuarioSistema
from .models import LogUsuarioSistema

admin.site.register(UsuarioSistema)
admin.site.register(LogUsuarioSistema)
