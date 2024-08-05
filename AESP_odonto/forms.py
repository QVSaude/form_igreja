from django.utils import timezone
from django import forms
from .models import AESP_odonto, Dependente
from django.forms import inlineformset_factory

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
            
class DependenteForm(forms.ModelForm):
    class Meta:
        model = Dependente
        fields = '__all__'
        
        
        def __init__(self, *args, **kwargs):
            super(DependenteForm, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'
       
# Define the formset
DependenteFormSet = inlineformset_factory(
    AESP_odonto, Dependente, form=DependenteForm, extra=1, can_delete=True
)     
