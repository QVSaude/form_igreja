from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('cemaderj/', include('AESP_odonto.urls')),
    path('crefito2/', include('empresas_AESP_odonto.urls')),
]
