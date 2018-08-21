"""mozio_providers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include

from rest_framework_swagger.views import get_swagger_view

from core import views

schema_view = get_swagger_view(title='Mozio API')

urlpatterns = [
    path('provider/', views.ProviderListView.as_view()),
    path('provider/', include('rest_auth.urls')),
    path('provider/registration/', include('rest_auth.registration.urls')),

    path('service-area/', views.ServiceAreaListView.as_view()),
    path('service-area/<int:pk>/', views.ServiceAreaDetailsView.as_view()),

    path('docs/', schema_view)
]
