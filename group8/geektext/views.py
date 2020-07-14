from django.shortcuts import render
from django.http import HttpResponse
from .models import Books

#Get books and display them
def index(request):
    b = Books.objects.all()
    
    return HttpResponse(b)