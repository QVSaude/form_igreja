from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('igreja/', include('AESP_odonto.urls')),
    path('aspem/', include('empresas_AESP_odonto.urls')),
]
