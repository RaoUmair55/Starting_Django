from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello from django, my first app")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("this is from about page")

def contact(request):
    return HttpResponse("contect")