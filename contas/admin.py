from django.contrib import admin
# importa do nosso diretorio as classes criadas
from .models import Categoria
from .models import Transacao

admin.site.register(Categoria)
admin.site.register(Transacao)
