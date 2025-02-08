from django.shortcuts import render

# Create your views here.
def new(request):
    return render(request,'newg/new_test.html')