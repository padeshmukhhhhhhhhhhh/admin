from django.shortcuts import render,redirect
from .models import customer
# Create your views here.
def index(request):
    data=customer.objects.all()
    dict={"data":data}
    
    return render(request,"index.html",dict)

def adddata(request):
    data=customer.objects.all()
    dict={"data":data}
    if request.method == "POST":
        print("post")
        name=request.POST['name']
        address=request.POST['address']
        city=request.POST['city']
        phone=request.POST['phone']
        email=request.POST['email']
        
        newuser=customer(name=name,Address=address,City=city,phone=phone,Email=email)
        newuser.save()
        return redirect("index")   
    
def update(request,id):
    if request.method=="POST":
        name=request.POST['name']
        address=request.POST['address']
        city=request.POST['city']
        phone=request.POST['phone']
        email=request.POST['email']
        data=customer(id=id,name=name,Address=address,City=city,phone=phone,Email=email)
        data.save()
        return redirect("index")

def delete(request,id):
    if request.method=="POST":
        data=customer.objects.filter(id=id)
        data.delete()
        return redirect("index")   
                   