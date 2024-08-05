
import csv
from django.shortcuts import render

from AESP_odonto.models import AESP_odonto, Dependente
from .forms import AESP_odontoForm, DependenteForm, DependenteFormSet
from django.utils import timezone
from django.contrib import messages


from django.core.mail import EmailMessage
from django.conf import settings


def create_aesp_odonto(request):
    if request.method == 'POST':
        titular_form  = AESP_odontoForm(request.POST)
        dependente_formset = DependenteFormSet(request.POST, queryset=Dependente.objects.none())
        print(titular_form.errors)
        if titular_form.is_valid() and dependente_formset.is_valid():
            titular = titular_form.save()
            dependentes = dependente_formset.save(commit=False)
            for dependente in dependentes:
                dependente.titular = titular
                dependente.save()


            # Retrieve the saved data from the database
            titular_data = AESP_odonto.objects.get(pk=titular.pk)
            dependentes_data = Dependente.objects.filter(titular=titular)
            
            print(titular_data)
            print(dependentes_data)
            
            
            # Save the data to a CSV file
            save_to_csv(titular_data, dependentes_data)

            
            
            # Enviar o arquivo CSV por e-mail
            filepath =  'AESP_odonto/data/Layout AESP ODONTO.csv'
            recipient_email = 'andersonmoura812@gmail.com'  # Substitua pelo e-mail do destinatário
            email_sent = send_email_with_csv(filepath, recipient_email)
            if email_sent:
                messages.success(request, 'Formulário enviado com sucesso e email enviado!')
            else:
                messages.warning(request, 'Formulário enviado, mas houve um problema ao enviar o email.')
        else:
            print(titular_form.errors)
            print(dependente_formset.errors)
    else:
        titular_form = AESP_odontoForm()
        dependente_formset = DependenteFormSet(queryset=Dependente.objects.none())
    return render(request, 'create_aesp_odonto1.html', {
            'form': titular_form,
            'dependente_formset': dependente_formset,
})




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
        
        'EMAIL': titular.EMAIL,
        'DDD': titular.DDD,
        'FONE': titular.FONE,
        'CPF': titular.CPF,
        'TIPO_LOGRADOURO': titular.TIPO_LOGRADOURO,
        'NOME_LOGRADOURO': titular.NOME_LOGRADOURO,
        'NUMERO': titular.NUMERO,
        'BAIRRO': titular.BAIRRO,
        'COMPLEMENTO': titular.COMPLEMENTO,
        'CIDADE': titular.CIDADE,
        'ESTADO': titular.ESTADO,
        'CEP': titular.CEP,
    }
    
    # Preparar dados dos dependentes
    dependentes_data = [{
        'NOME': dependente.NOME,
        'NOME_MAE': dependente.NOME_MAE,
        'DATA_NASCIMENTO': dependente.DATA_NASCIMENTO,
        'CPF_DEPENDENTE': dependente.CPF_DEPENDENTE,
        'SEXO': dependente.SEXO,
        'ESTADO_CIVIL': dependente.ESTADO_CIVIL,
        'GRAU_DEPENDENCIA': dependente.GRAU_DEPENDENCIA,
        'RG': dependente.RG,
        'ORGAO_EMISSOR': dependente.ORGAO_EMISSOR
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








# def save_to_csv(data):
#     csv_file_path = 'AESP_odonto/data/Layout AESP ODONTO.csv'
    
#     # Ler o arquivo CSV existente
#     with open(csv_file_path, mode='r', newline='', encoding='utf-8-sig') as file:
#         reader = csv.reader(file, delimiter=';')
#         header = next(reader)  # Ler a primeira linha como cabeçalho
#         #print(f'Header: {header}')
#         existing_data = list(reader)

#     # Verificar se os campos do cabeçalho estão presentes em data
#     #for field in header:
#         #if field not in data:
#             #print(f'Aviso: O campo "{field}" não está presente em data.')

#     # Adicionar uma nova linha com os dados do formulário
#     new_row = [data.get(field, '') for field in header]
#     #print(f'Nova linha: {new_row}')

#     # Escrever o arquivo CSV atualizado
#     with open(csv_file_path, mode='w', newline='', encoding='utf-8-sig') as file:
#         writer = csv.writer(file, delimiter=';')
#         writer.writerow(header)  # Escrever o cabeçalho
#         writer.writerows(existing_data)  # Escrever os dados existentes
#         writer.writerow(new_row)  # Adicionar a nova linha
#         #print(f'Linha adicionada: {new_row}')
#     return csv_file_path


def send_email_with_csv(file_path, recipient_email):
    subject = 'Arquivo CSV'
    body = 'Segue em anexo o arquivo CSV solicitado.'
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