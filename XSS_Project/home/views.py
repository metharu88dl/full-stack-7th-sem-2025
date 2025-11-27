from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')

def nameRef(request):
    if request.method=="POST":
        name=request.POST.get('name')
        if not name:
            return HttpResponse("Please provide a name.")
        
        name1=name.lower()
        if "script" in name1:
            name2=name1.replace("script","")
            return HttpResponse(f"Hello {name2}! Alert('Hacked')")
        else:
            return HttpResponse(f"Hello {name}!")
