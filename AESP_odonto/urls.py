from django.urls import path
from .views import create_aesp_odonto, desativar_dependent, desativar_titular, list_aesp_odonto

urlpatterns = [
    path('create/', create_aesp_odonto, name='create_aesp_odonto'),
    path('list/', list_aesp_odonto, name='list_aesp_odonto'),
    path('desativar_titular/<int:user_id>/', desativar_titular, name='desativar_titular'),
    path('desativar_dependent/<int:user_id>/', desativar_dependent, name='desativar_dependent'),
]
