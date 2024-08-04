from django.utils import timezone
from django import forms
from .models import AESP_odonto

class AESP_odontoForm(forms.ModelForm):
    class Meta:
        model = AESP_odonto
        fields = '__all__'
        widgets = {
            'TIPO': forms.Select(attrs={'id': 'tipo-select'}),
        }

    def __init__(self, *args, **kwargs):
        super(AESP_odontoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
