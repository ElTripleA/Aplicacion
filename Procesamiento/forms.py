from django import forms

from models import RegistroCovid


class visual(forms.ModelForm):
    class Meta:
        model = RegistroCovid
        fields = '__all__'