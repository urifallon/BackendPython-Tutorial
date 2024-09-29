from django.shortcuts import render
from django.http import HttpResponse

def reqHome(request):
    return render(request, 'home.html')

