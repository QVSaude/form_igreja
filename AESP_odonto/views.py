
import csv
from django.shortcuts import render
from .forms import AESP_odontoForm
from django.utils import timezone
from django.contrib import messages


from django.core.mail import EmailMessage
from django.conf import settings


def create_aesp_odonto(request):
    if request.method == 'POST':
        form = AESP_odontoForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            # Salvar as informações no arquivo CSV    
            print(form.cleaned_data)        
            save_to_csv(form.cleaned_data)

           
            filepath =  'AESP_odonto/data/Layout AESP ODONTO.csv'

            # Enviar o arquivo CSV por e-mail
            recipient_email = 'andersonmoura812@gmail.com'  # Substitua pelo e-mail do destinatário
            email_sent = send_email_with_csv(filepath, recipient_email)
            if email_sent:
                messages.success(request, 'Formulário enviado com sucesso e email enviado!')
            else:
                messages.warning(request, 'Formulário enviado, mas houve um problema ao enviar o email.')
    else:
        form = AESP_odontoForm()
    return render(request, 'create_aesp_odonto1.html', {'form': form})


def save_to_csv(data):
    csv_file_path = 'AESP_odonto/data/Layout AESP ODONTO.csv'

    #print(f'linha 24 {data}')  # Verificar o conteúdo de data
    
    # Ler o arquivo CSV existente
    with open(csv_file_path, mode='r', newline='', encoding='utf-8-sig') as file:
        reader = csv.reader(file, delimiter=';')
        header = next(reader)  # Ler a primeira linha como cabeçalho
        #print(f'Header: {header}')
        existing_data = list(reader)

    # Verificar se os campos do cabeçalho estão presentes em data
    #for field in header:
        #if field not in data:
            #print(f'Aviso: O campo "{field}" não está presente em data.')

    # Adicionar uma nova linha com os dados do formulário
    new_row = [data.get(field, '') for field in header]
    #print(f'Nova linha: {new_row}')

    # Escrever o arquivo CSV atualizado
    with open(csv_file_path, mode='w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(header)  # Escrever o cabeçalho
        writer.writerows(existing_data)  # Escrever os dados existentes
        writer.writerow(new_row)  # Adicionar a nova linha
        #print(f'Linha adicionada: {new_row}')
    return csv_file_path


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