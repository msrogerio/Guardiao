from django.contrib import admin

from .models import Bairro
from .models import Endereco
from .models import Conjunto
from .models import Caracteristicas
from .models import DocumentosUnico
from .models import Imagen
from .models import Individuo
from .models import Tatuagem

admin.site.register(Bairro)
admin.site.register(Endereco)
admin.site.register(Conjunto)
admin.site.register(Caracteristicas)
admin.site.register(DocumentosUnico)
admin.site.register(Imagen)
admin.site.register(Individuo)
admin.site.register(Tatuagem)