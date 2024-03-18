from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.db.models import Q
from .models import *
import datetime
import pickle
import numpy as np
import os
import json
import termcolor
import smtplib
import prepredict as pr
import CurrentStats
# import CancerModel
# import PdfConverter
# from PdfConverter import PDFPageCountError
import DiseasePred
from django.http import HttpResponse

# Create your views here.

# Create your views here.
def Index(request):
    return render(request,"index.html")
def commanpage(request):
    return render(request,"Commanpages/Commanpage.html")
def Login(request):
    msg=""
    try:
        if request.method == 'POST':
            username = request.POST.get('Username')
            password = request.POST.get('Password')
            request.session["uname"] =username
            user = authenticate(username=username,password=password)
            print(user)
            print(user.userType)
            if user is not None:
                if user.userType =="Patient":
                    # login(request,user)
                    messages.info(request,"Login successfull")
                    return redirect('/PatientIndex')
                if user.userType =="Admin":
                    # login(request,user)
                    messages.info(request,"Login successfull")
                    return redirect('/Adminpage')
                if user.userType =="Doctor":
                    # login(request,user)
                    messages.info(request,"Login successfull")
                    return redirect('/DoctorIndex')
            else:
                messages.info(request,"invalid username or password")
                messages.error(request,'Invalid Credentials')
    except:
        msg="invalid username or password"
    return render(request,"Commanpages/Login.html",{"msg":msg})
def Patientreg(request):
    if request.POST:
        name=request.POST["name"]
        
        email=request.POST["email"]
        phone=request.POST["phone"]
        address=request.POST["address"]
        dob=request.POST["dob"]
        
        uname=request.POST["email"]
        password=request.POST["password"]
        img=request.FILES["img"]
        if not CustomUser.objects.filter(username=email).exists(): 
            login=CustomUser.objects.create_user(username=email,password=password,userType='Patient',viewpassword=password)
            login.save()
            obj=Userregistration.objects.create(user=login,name=name,email=email,address=address,phone=phone,dob=dob,uname=uname,img=img)
            obj.save()
            messages.info(request,"user Added successful")
        else:
            messages.info(request,"user already added")
    return render(request,"Commanpages/Patientreg.html")
def Doctorreg(request):
    if request.POST:
        name=request.POST["name"]
        desig=request.POST.get("desig")
        email=request.POST["email"]
        phone=request.POST["phone"]
        address=request.POST["address"]
        dob=request.POST["dob"]
        
        uname=request.POST["email"]
        password=request.POST["password"]
        img=request.FILES["img"]
        if not CustomUser.objects.filter(username=email).exists(): 
            login=CustomUser.objects.create_user(username=email,password=password,userType='Doctor',viewpassword=password)
            login.save()
            obj=Doctorregistration.objects.create(user=login,name=name,desig=desig,email=email,address=address,phone=phone,dob=dob,uname=uname,img=img)
            obj.save()
            messages.info(request,"user Added successful")
        else:
            messages.info(request,"user already added")
    return render(request,"Commanpages/Doctorreg.html")


######################Admin Pages############################

def adminindex(request):
    return render(request,"Admin/adminindex.html")


######################User Pages############################

def PatientIndex(request):
    return render(request,"Patient/PatientIndex.html")
def Patientpage(request):
    return render(request,"Patient/Patientpage.html")
def PatientViewDoctor(request):
    data=Doctorregistration.objects.all()
    return render(request,"Patient/PatientViewDoctor.html",{"data":data})
def Uploadimage(request):
    msg=""
    with open("CKD_Model", "rb") as f:
        decisionTree = pickle.load(f)
    if request.POST:
        # submitted_values = request.form
        sg = str(float(request.POST["sg"]))
        albumin = str(float(request.POST["albumin"]))
        hemoglobin = str(float(request.POST["hemoglobin"]))
        pcv = str(float(request.POST["pcv"]))
        hypertension = str(float(request.POST["hypertension"]))
        sc = str(float(request.POST["sc"]))

        ckd_inputs1 = [sg, albumin, sc, hemoglobin, pcv, hypertension]
        prediction = decisionTree.predict([ckd_inputs1])
       
        prediction=pr.prepredict(ckd_inputs1)
        print("**************             ", prediction)
        if  prediction==0:
            msg="No desease"
        else:
            msg="Cronic Kidney Desease"
        print(msg)

        
    return render(request,"Patient/Uploadimage.html",{"msg":msg})
   
def bookdoctor(requ):
    if requ.POST:
        id=requ.GET["id"]
        username=requ.session["uname"]
        request=requ.POST["request"]
        bookingdate=requ.POST["bookingdate"]
        councelr=Doctorregistration.objects.get(id=id)
        usr=Userregistration.objects.get(email=username)
        obj=Booking.objects.create(councelr=councelr,usr=usr,request=request,bookingdate=bookingdate,status='booked')
        obj.save()

    return render(requ,"Patient/bookdoctor.html")

######################Doctor Pages############################

def DoctorIndex(request):
    return render(request,"Doctor/DoctorIndex.html")
def Doctorpage(request):
    return render(request,"Doctor/Doctorpage.html")
def ViewBooking(request):
    uname=request.session["uname"]
    
    data=Booking.objects.filter(councelr_id__email=uname)
    print(data)
    return render(request,"Doctor/ViewBooking.html",{"data":data})
def Viewimage(request):
    email=request.GET["email"]
    
    data=Requestuser.objects.filter(user_id__username=email)
    print(data)
    return render(request,"Doctor/Viewimage.html",{"data":data})

def demofile(request):
    if request.POST:
        name=request.POST["t1"]
        age=request.POST["t2"]
        addr=request.POST["t3"]
        obj=Demomodel.objects.create(name=name,age=age,address=addr)
        obj.save()

