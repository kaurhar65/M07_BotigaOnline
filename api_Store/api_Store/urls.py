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
from cataleg import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cataleg/get/', views.get_Prod, name="get"),
    path('cataleg/get/<int:pk>/', views.get_Prod_ById, name="getById"),
    path('cataleg/delete/<int:pk>/', views.delete_Prod_ById, name="deleteById"),
    path('product/add/', views.add_Prod, name="addProd"),
    path('product/update/<int:pk>/', views.update_Prod, name="updateProd")
]
