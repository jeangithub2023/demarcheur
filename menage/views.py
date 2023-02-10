from django.shortcuts import render, get_object_or_404

from menage.models import Menus

# Create your views here.

def index(request):
    menus=Menus.objects.all()
    context={
        "menus": menus
    }
    return render(request,'menage/index.html', context)

def detail(request, id):
    service=get_object_or_404(Menus,id=id)
    context={
        "service": service
    }
    return render(request,'menage/detail.html', context)

def contact(request):
    return render(request, 'menage/contact.html')