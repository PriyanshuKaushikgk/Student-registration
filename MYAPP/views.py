from django.shortcuts import render,HttpResponse
from .models import Student


# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        gender = request.POST['gender']
        image = request.FILES['image']
        Student(name=name,email=email,address=address,gender=gender,image=image).save()
        return HttpResponse("SUCCESSFULLY SAVED ")
    return render(request,'index.html')