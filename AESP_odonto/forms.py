from django import forms
from .models import AESP_odonto

class AESP_odontoForm(forms.ModelForm):
    class Meta:
        model = AESP_odonto
        fields = '__all__'