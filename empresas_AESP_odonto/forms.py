from django.utils import timezone
from django import forms
from .models import AESP_odonto_empresa, Dependente
from django.forms import inlineformset_factory

class AESP_odontoForm(forms.ModelForm):
    class Meta:
        model = AESP_odonto_empresa
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AESP_odontoForm, self).__init__(*args, **kwargs)
        readonly_fields = ['CONDICAO', 'NRO_CONTRATO', 'DATA_MOVIMENTO', 'DATA_INICIO_UTILIZACAO', 'CODIGOPLANODATASYS', 'TIPO']
        for field_name in readonly_fields:
            self.fields[field_name].widget.attrs.update({'readonly': 'readonly', 'class': 'form-control'})

        self.fields['STATUS'].widget.attrs.update({'id': 'STATUS'})
        
        self.fields['CEP'].widget.attrs.update({'id': 'id_CEP'})
        self.fields['NOME_LOGRADOURO'].widget.attrs.update({'id': 'id_NOME_LOGRADOURO'})
        self.fields['COMPLEMENTO'].widget.attrs.update({'id': 'id_COMPLEMENTO'})
        self.fields['BAIRRO'].widget.attrs.update({'id': 'id_BAIRRO'})
        self.fields['CIDADE'].widget.attrs.update({'id': 'id_CIDADE'})
        self.fields['ESTADO'].widget.attrs.update({'id': 'id_ESTADO'})
        
        self.fields['DATA_NASCIMENTO'].widget.attrs.update({'class': 'id_DATA_NASCIMENTO', 'placeholder': '00/00/0000'})
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
class DependenteForm(forms.ModelForm):
    class Meta:
        model = Dependente
        fields = '__all__'
        
        
    def __init__(self, *args, **kwargs):
        super(DependenteForm, self).__init__(*args, **kwargs)
        self.fields['TIPO'].widget.attrs.update({'readonly': 'readonly', 'class': 'form-control'})
        self.fields['DATA_NASCIMENTO'].widget.attrs.update({ 'placeholder':'00/00/0000'})
        

        
        for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'
                if field_name == 'DATA_NASCIMENTO':
                    field.widget.attrs['class'] = 'DATA_NASCIMENTO_DEP form-control'
    
       
# Define the formset
DependenteFormSet = inlineformset_factory(
    AESP_odonto_empresa, Dependente, form=DependenteForm, extra=1, can_delete=False
)     
