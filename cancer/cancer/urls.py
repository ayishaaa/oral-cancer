"""cancer URL Configuration

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
from django.conf import settings
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('login/',views.login),
    path('adminheader/',views.adminheader),
    path('managehealthworker/',views.managehealthworker),
    path('manageexpert/',views.manageexpert),
    path('registerexpert/',views.registerexpert),
    path('registerworker/',views.registerworker),
    path('addexpert/',views.addexpert),
    path('addworker/',views.addworker),
    path('addexpert1/',views.addexpert1),
    path('addworker1/',views.addworker1),
    path('removeworker/',views.removeworker),
    path('removeexpert/',views.removeexpert),
    path('verifyworker/',views.verifyworker),
    path('verifyexpert/',views.verifyexpert),
    path('removeworker1/<str:id>',views.removeworker1),
    path('removeexpert1/<str:id>',views.removeexpert1),
    path('verifyexpert1/<str:id>',views.verifyexpert1),
    path('verifyexpert2/<str:id>',views.verifyexpert2),
    path('verifyworker1/<str:id>',views.verifyworker1),
    path('verifyworker2/<str:id>',views.verifyworker2),
    path('patientheader/',views.patientheader),
    path('patientbasic/',views.patientbasic),
    path('registerpatient/',views.registerpatient)
]
