from django.forms import ModelForm
from .models import produto

class produtoForm(ModelForm):
    class Meta:
        model = produto
        fields = ['data','nome','valor','obs','categoria']