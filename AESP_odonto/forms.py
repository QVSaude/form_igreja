from django.utils import timezone
from django import forms
from .models import AESP_odonto, Dependente
from django.forms import inlineformset_factory

class AESP_odontoForm(forms.ModelForm):
    class Meta:
        model = AESP_odonto
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AESP_odontoForm, self).__init__(*args, **kwargs)
        self.fields['CONDICAO'].widget.attrs.update({'readonly': 'readonly', 'class': 'form-control'})
        self.fields['NRO_CONTRATO'].widget.attrs.update({'readonly': 'readonly', 'class': 'form-control'})
        self.fields['DATA_MOVIMENTO'].widget.attrs.update({'readonly': 'readonly', 'class': 'form-control'})
        self.fields['DATA_INICIO_UTILIZACAO'].widget.attrs.update({'readonly': 'readonly', 'class': 'form-control'})
        self.fields['CODIGOPLANODATASYS'].widget.attrs.update({'readonly': 'readonly', 'class': 'form-control'})
        self.fields['TIPO'].widget.attrs.update({'readonly': 'readonly', 'class': 'form-control'})
        
        self.fields['CEP'].widget.attrs.update({'id': 'id_CEP'})
        self.fields['NOME_LOGRADOURO'].widget.attrs.update({'id': 'id_NOME_LOGRADOURO'})
        self.fields['COMPLEMENTO'].widget.attrs.update({'id': 'id_COMPLEMENTO'})
        self.fields['BAIRRO'].widget.attrs.update({'id': 'id_BAIRRO'})
        self.fields['CIDADE'].widget.attrs.update({'id': 'id_CIDADE'})
        self.fields['ESTADO'].widget.attrs.update({'id': 'id_ESTADO'})
        
        self.fields['DATA_NASCIMENTO'].widget.attrs.update({'id': 'id_DATA_NASCIMENTO'})
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
class DependenteForm(forms.ModelForm):
    class Meta:
        model = Dependente
        fields = '__all__'
        
        
    def __init__(self, *args, **kwargs):
        super(DependenteForm, self).__init__(*args, **kwargs)
        self.fields['TIPO'].widget.attrs.update({'readonly': 'readonly', 'class': 'form-control'})
        for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'
       
# Define the formset
DependenteFormSet = inlineformset_factory(
    AESP_odonto, Dependente, form=DependenteForm, extra=1, can_delete=False
)     
