from django.shortcuts import render

# Create your views here.

def homeapp(request):
    return render(request, 'firstApp/Home.html')