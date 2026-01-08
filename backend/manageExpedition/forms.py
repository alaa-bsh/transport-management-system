from django import forms
from .models import Expedition, Facture, Tournée


class ExpeditionForm(forms.ModelForm):
    class Meta:
        model = Expedition
        fields="__all__"


class TournéeForm(forms.ModelForm):
    class Meta:
        model = Tournée
        fields="__all__"



class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields="__all__"