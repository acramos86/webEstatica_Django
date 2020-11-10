"""proyectoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from proyectoDjango.views import inicio, talleres, incubadora, duda, solDirecto, humeda, guias, cuidados

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name = 'index'),
    path('talleres/', talleres, name = 'talleres'),
    path('incubadora/', incubadora, name = 'incubadora'),
    path('duda/', duda, name = 'duda'),
    path('solDirecto/', solDirecto, name = 'solDirecto'),
    path('humeda/', humeda, name = 'humeda'),
    path('guias/', guias, name ='guias'),
    path('cuidados/', cuidados, name = 'cuidados')
]
