from django.shortcuts import render, redirect
from .forms import AESP_odontoForm

def create_aesp_odonto(request):
    if request.method == 'POST':
        form = AESP_odontoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirecionar para uma página de sucesso
    else:
        form = AESP_odontoForm()
    return render(request, 'create_aesp_odonto1.html', {'form': form})
