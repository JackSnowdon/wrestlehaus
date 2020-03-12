from django import forms
from .models import *

class WrestlerForm(forms.ModelForm):

    class Meta:
        model = Wrestler
        fields = '__all__'
        labels = {
            "dex": "Dexterity",
        }


class MoveForm(forms.ModelForm):

    class Meta:
        model = Move
        fields = '__all__'


class PromotionForm(forms.ModelForm):

    class Meta:
        model = Promotion
        fields = '__all__'


class MatchForm(forms.ModelForm):

    class Meta:
        model = Match
        fields = ['fighters']