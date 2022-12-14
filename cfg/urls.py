"""ProyectoSITU URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.urls import include
from appSITUweb import views as vw_pasajeros
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', vw_pasajeros.home_view, name='home'),
    path('admin/', admin.site.urls),

    path('pasajeros/', vw_pasajeros.pasajeros, name='pasajeros'),
    path('pasajerosEdit/<id>', vw_pasajeros.pasajeros_edit, name='pasajerosEdit'),
    path('pasajerosCreate', vw_pasajeros.pasajeros_create, name='pasajerosCreate'),
    path('pasajerosDelete/<id>', vw_pasajeros.pasajeros_delete, name='pasajerosDelete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)