from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import book
from .models import teacher,test


# Create your views here.
def index(request):
    if request.method == "POST":
     text1 = request.POST.get("text1")
     text2 = request.POST.get("text2")
     text3 = request.POST.get("text3")
     test.objects.create(text1 = text1,text2 = text2, text3 = text3)
     return redirect("main")
    books = book.objects.all()
    teachers = teacher.objects.all()
    return render(request,'main/index.html',{'books': books,'teachers':teachers})

def about(request):
    return render(request,'main/about.html')

def newg(request):
   return render(request,'newg/new_test.html')