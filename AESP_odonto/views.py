import csv
import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader

from AESP_odonto.models import AESP_odonto, Dependente
from .forms import AESP_odontoForm, DependenteForm, DependenteFormSet
from django.contrib import messages

from django.core.mail import EmailMessage
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


def create_aesp_odonto(request):
    if request.method == 'POST':
        titular_form = AESP_odontoForm(request.POST)
        dependente_formset = DependenteFormSet(request.POST)
        
        for form in dependente_formset:
            print(form.prefix)
            print(form.is_valid())
                
        if titular_form.is_valid() and dependente_formset.is_valid():
            titular = titular_form.save()
            dependentes = dependente_formset.save(commit=False)
            for dependente in dependentes:
                dependente.titular = titular
                dependente.save()

            # Retrieve the saved data from the database
            titular_data = AESP_odonto.objects.get(pk=titular.pk)
            dependentes_data = Dependente.objects.filter(titular=titular)

            # Save the data to a CSV file
            save_to_csv(titular_data, dependentes_data)

            # Enviar o arquivo CSV por e-mail
            filepath = 'AESP_odonto/data/Layout AESP ODONTO.csv'
            recipient_email = 'movimentacao@qvsaude.com.br'  # Substitua pelo e-mail do destinatário para teste
            email_sent = send_email_with_csv(filepath, recipient_email)

            if email_sent:
                messages.success(request, 'Formulário enviado com sucesso e email enviado!')
            else:
                messages.warning(request, 'Formulário enviado, mas houve um problema ao enviar o email.')
        else:
            # Exibindo erros para o formulário titular
            if titular_form.errors:
                messages.warning(request, f'(ERRO) {titular_form.errors}')
            
            # Exibindo erros para o formset de dependentes
            if dependente_formset.errors:
                messages.warning(request, f'(ERRO) {dependente_formset.errors}')
                for form in dependente_formset:
                    if 'DATA_NASCIMENTO' in form.errors:
                        if form.errors['DATA_NASCIMENTO'] == ['Informe uma data válida.']:
                            messages.warning(request, '(ERRO) A DATA NASCIMENTO do dependente deve ter a formatação: 00/00/0000, verifique e tente novamente')
                            break  # Para ao encontrar o erro que queremos destacar
    else:
        titular_form = AESP_odontoForm()
        dependente_formset = DependenteFormSet(queryset=Dependente.objects.none())
    
    return render(request, 'create_aesp_odonto1.html', {
        'form': titular_form,
        'dependente_formset': dependente_formset,
    })

def list_aesp_odonto(request):
    titular = AESP_odonto.objects.values()
    dependente = Dependente.objects.values()
    context = {
        'Titulares': titular,
        'dependentes': dependente
    }
    template = loader.get_template('list_aesp_odonto.html')
    
    
    return HttpResponse(template.render(context, request))


@csrf_exempt
def desativar_titular(request, user_id):
    if request.method == 'POST':
        try:
            titular = get_object_or_404(AESP_odonto, id=user_id)
            titular.STATUS = 'Desativado'
            titular.save()
            return JsonResponse({'success': True})
        except titular.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Benenficiario não encontrado.'})
    return JsonResponse({'success': False, 'error': 'Método não permitido.'})

@csrf_exempt
def desativar_dependent(request, user_id):
    if request.method == 'POST':
        try:
            titular = get_object_or_404(Dependente, id=user_id)
            titular.STATUS = 'Desativado'
            titular.save()
            return JsonResponse({'success': True})
        except titular.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Benenficiario não encontrado.'})
    return JsonResponse({'success': False, 'error': 'Método não permitido.'})


def save_to_csv(titular, dependentes):
    csv_file_path = 'AESP_odonto/data/Layout AESP ODONTO.csv'
    
    # Ler o arquivo CSV existente
    with open(csv_file_path, mode='r', newline='', encoding='utf-8-sig') as file:
        reader = csv.reader(file, delimiter=';')
        header = next(reader)  # Ler a primeira linha como cabeçalho
        existing_data = list(reader)

    # Preparar dados do titular
    titular_data = {
        'CONDICAO': titular.CONDICAO,
        'NRO_CONTRATO': titular.NRO_CONTRATO,
        'DATA_MOVIMENTO': titular.DATA_MOVIMENTO,
        'DATA_INICIO_UTILIZACAO': titular.DATA_INICIO_UTILIZACAO,
        'TIPO': titular.TIPO,
        'NOME': titular.NOME,
        'NOME_MAE': titular.NOME_MAE,
        'DATA_NASCIMENTO': titular.DATA_NASCIMENTO,
        'RG': titular.RG,
        'UF_RG': titular.UF_RG,
        'CPF': titular.CPF,
        'SEXO': titular.SEXO,
        'ESTADO_CIVIL': titular.ESTADO_CIVIL,
        
        'TIPO_LOGRADOURO': titular.TIPO_LOGRADOURO,
        'NOME_LOGRADOURO': titular.NOME_LOGRADOURO,
        'NUMERO': titular.NUMERO,
        'BAIRRO': titular.BAIRRO,
        'COMPLEMENTO': titular.COMPLEMENTO,
        'CIDADE': titular.CIDADE,
        'ESTADO': titular.ESTADO,
        'CEP': titular.CEP,
        'EMAIL': titular.EMAIL,
        'DDD': titular.DDD,
        'FONE': titular.FONE,
        'CODIGOPLANODATASYS': titular.CODIGOPLANODATASYS,
        
    }
    
    # Preparar dados dos dependentes
    dependentes_data = [{
        'CONDICAO': titular.CONDICAO,
        'NRO_CONTRATO': titular.NRO_CONTRATO,
        'CPF_TITULAR': titular.CPF,
        
        'TIPO': dependente.TIPO,
        'NOME': dependente.NOME,
        'NOME_MAE': dependente.NOME_MAE,
        'DATA_NASCIMENTO': dependente.DATA_NASCIMENTO,
        'CPF': dependente.CPF_DEPENDENTE,
        'SEXO': dependente.SEXO,
        'ESTADO_CIVIL': dependente.ESTADO_CIVIL,
        'GRAU_DEPENDENCIA': dependente.GRAU_DEPENDENCIA,
        'RG': dependente.RG,
        'ORGAO_EMISSOR': dependente.ORGAO_EMISSOR,
        
        'TIPO_LOGRADOURO': titular.TIPO_LOGRADOURO,
        'NOME_LOGRADOURO': titular.NOME_LOGRADOURO,
        'NUMERO': titular.NUMERO,
        'BAIRRO': titular.BAIRRO,
        'COMPLEMENTO': titular.COMPLEMENTO,
        'CIDADE': titular.CIDADE,
        'ESTADO': titular.ESTADO,
        'CEP': titular.CEP,
        'EMAIL': titular.EMAIL,
        'DDD': titular.DDD,
        'FONE': titular.FONE,
        'CODIGOPLANODATASYS': titular.CODIGOPLANODATASYS,
    } for dependente in dependentes]

    # Adicionar uma nova linha com os dados do titular
    new_row = [titular_data.get(field, '') for field in header]

    # Escrever o arquivo CSV atualizado
    with open(csv_file_path, mode='w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(header)  # Escrever o cabeçalho
        writer.writerows(existing_data)  # Escrever os dados existentes
        writer.writerow(new_row)  # Adicionar a nova linha do titular

        # Adicionar linhas dos dependentes
        for dependente_data in dependentes_data:
            dependente_row = [dependente_data.get(field, '') for field in header]
            writer.writerow(dependente_row)  # Adicionar a nova linha do dependente

    return csv_file_path

def data():
    current_date = datetime.now()
    data_em_texto = '{}/{}/{}'.format(current_date.day,current_date.month,
    current_date.year)
    return data_em_texto

def send_email_with_csv(file_path, recipient_email):
    subject = 'Arquivo CSV Beneficiarios AESP'
    body = f'Segue em anexo o arquivo CSV dos novos beneficiarios {data()}'
    email = EmailMessage(subject, body, settings.DEFAULT_FROM_EMAIL, [recipient_email])
    
    # Adicionar o arquivo CSV como anexo
    email.attach_file(file_path)
    
    try:
        # Enviar o e-mail
        email.send()
        return True  # Email enviado com sucesso
    except Exception as e:
        print(f"Erro ao enviar o email: {e}")
        return False  # Falha no envio do email