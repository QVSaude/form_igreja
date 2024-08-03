from django.urls import path
from .views import create_aesp_odonto

urlpatterns = [
    path('create/', create_aesp_odonto, name='create_aesp_odonto'),
]
