from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Post,Poll,Roll,Category,Intial
def Home(request):
    Posts = Post.objects.all()
    context={
        "Posts": Posts,
    }
    name="prasanna"
    # colours=["red","green","pink","blue"]
    return render(request,"demo/home.html",context)


def punnam(request):
    Polls = Poll.objects.all()
    context={
        "Polls" : Polls
    }
    name="Prasanna"
    return render(request,"demo/punnam.html",context)

def ramala(request):
    Rolls = Roll.objects.all()
    context={
        "Rolls" : Rolls
    }
    return render(request,"demo/ramala.html",context)

def intial(request):
    Categories=Category.objects.all()
    Intials = Intial.objects.all()
    context={
        "Categories" : Categories,
        "Intials": Intials
    }
    return render(request,"demo/intial.html",context)

def category(request,id):
    Categories = Category.objects.get(id=id)
    Intials = Intial.objects.filter(Category=Categories)
    context={
        "Categories" : Categories,
        "Intials": Intials
    }
    return render(request,"demo/category.html",context)






