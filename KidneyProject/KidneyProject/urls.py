"""
URL configuration for KidneyProject project.

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
from KidneyApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.Index),
     path("Commanpage",views.commanpage),
     path("login/",views.Login),
     path("Patientreg",views.Patientreg),
     path("Patientreg/",views.Patientreg),
     path("Doctorreg",views.Doctorreg),
          path("Doctorreg/",views.Doctorreg),
     #############Admin
     path("adminindex",views.adminindex),

     ########Patient

     path("PatientIndex",views.PatientIndex),
     path("Patientpage",views.Patientpage),
     path("PatientViewDoctor",views.PatientViewDoctor),
     path("Uploadimage",views.Uploadimage),
     path("bookdoctor",views.bookdoctor),

     
     ########Doctor

     path("DoctorIndex",views.DoctorIndex),
     path("Doctorpage",views.Doctorpage),
     path("ViewBooking",views.ViewBooking),
      path("Viewimage",views.Viewimage),
]
