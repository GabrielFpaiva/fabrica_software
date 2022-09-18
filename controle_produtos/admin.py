from django.contrib import admin
from .models import categoria
from .models import produto

admin.site.register(categoria)
admin.site.register(produto)