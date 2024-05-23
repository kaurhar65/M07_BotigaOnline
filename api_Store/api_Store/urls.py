"""
URL configuration for api_Store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from comandes import views


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # COMANDES
    path('comandes/get/', views.get_Comand, name="get"),
    path('comandes/get/<int:pk>/', views.get_Comand_ById, name="getById"),
    
    path('comandes/get/client/<int:client_id>/', views.get_Comand_ByClient, name="getByClient"),
    path('comandes/get/actives/', views.get_Comand_Active, name="getByActive"),
    
    path('comandes/delete/<int:pk>/', views.delete_Comand_ById, name="deleteById"),
]
