"""
URL configuration for user_defined_filter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register_agent/', register_agent, name='register_agent'),
    path('register_cust/', register_cust, name='register_cust'),
    path('display_agent/', display_agent, name='display_agent'),
    path('display_cust/', display_cust, name='display_cust'),
    path('retrive/', retrive, name='retrive'),
    path('user_defined_filter/', user_defined_filter, name='user_defined_filter'),
]
