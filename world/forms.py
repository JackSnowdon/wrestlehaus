from django import forms
from .models import *

class WrestlerForm(forms.ModelForm):

    class Meta:
        model = Wrestler
        fields = '__all__'
        labels = {
            "dex": "Dexterity",
        }
