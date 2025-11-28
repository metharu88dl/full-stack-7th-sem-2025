from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def bio_data_form(request):
    return render(request,'index.html')

def display_biodata(request):
    if request.method=="POST":
        name=request.POST.get("name")
        age=request.POST.get('age')
        email=request.POST.get('email')
        address=request.POST.get('address')
        context={
            "name":name,
            "age":age,
            "email": email,
            "address":address,
        }
        return render(request,'display_biodata.html',context)
    else:
        return HttpResponse("Invalid request")

