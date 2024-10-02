from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AESP_odonto.urls')),
    path('empresa/', include('empresas_AESP_odonto.urls')),
]
