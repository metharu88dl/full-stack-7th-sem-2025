from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def bio_data_form(request):
    return render(request, 'bio_data_form.html')

def display_bio_data(request):
    if(request.method == 'POST'):
        name=request.POST.get("name")
        age=request.POST.get("age")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        address=request.POST.get("address")
        context={
            'name':name,
            'age':age,
            'phone':phone,
            'email':email,
            'address':address
        }
        return render(request,'display_bio_data.html',context)
    else:
        return HttpResponse("Invalid Method")
