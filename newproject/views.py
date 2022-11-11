from django.shortcuts import render
from django.shortcuts import HttpResponse

def Menu(requset):
    return render(requset,"index.html",{})