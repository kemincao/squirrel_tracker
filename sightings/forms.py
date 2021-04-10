
from django.forms import ModelForm
from .models import Squirrels

class SquirrelForm(ModelForm):
    class Meta:
        moedl = Squirrels
        fields = '__all__'
