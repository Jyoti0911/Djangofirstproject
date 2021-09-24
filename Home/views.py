from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from datetime import date, datetime
from Home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
   
    return render(request, 'index.htm')
    #return HttpResponse("this is Homepage")

def about(request):
    return render(request, 'about.htm')
def contact(request):
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email, phone=phone, desc=desc)
        contact.save()
        messages.success(request, 'message sent successfully.')
    
    return render(request, 'contact.htm')
