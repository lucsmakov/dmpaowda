"""
URL configuration for k2mjcar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/registrar', Registrar.as_view(),name='url_registrar'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', home, name='url_principal'),
    path('cadastro_cliente', cadastro_Cliente, name='url_cadastro_cliente'),
    path('listagem_clientes', listagem_clientes, name='url_listagem_clientes'),
    path('cadastro_veiculo', cadastro_Veiculo, name='url_cadastro_veiculo'),
    path('listagem_veiculos', listagem_veiculos, name='url_listagem_veiculos'),
    path('cadastro_fabricante', cadastro_Fabricante, name='url_cadastro_fabricante'),
    path('listagem_fabricantes', listagem_fabricantes, name='url_listagem_fabricantes'),
    path("atualiza_cliente/<int:id>/", atualiza_cliente, name= 'url_atualiza_cliente'),
    path("exclui_cliente/<int:id>/", exclui_cliente, name="url_exclui_cliente")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
