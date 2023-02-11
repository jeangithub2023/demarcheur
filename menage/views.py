from django.shortcuts import render, get_object_or_404

from menage.models import Menus, Services

# Create your views here.

def index(request):
    menus=Menus.objects.all()
    context={
        "menus": menus
    }
    return render(request,'menage/index.html', context)

def detail(request, id):
    menu=get_object_or_404(Menus,id=id)
    print(menu)
    services=Services.objects.filter(menu=menu)
    print(services)
    context={
        "menu": menu,
        "services": services
    }
    return render(request,'menage/detail.html', context)

def contact(request):
    return render(request, 'menage/contact.html')

def menage(request,id):
    service=get_object_or_404(Services,id=id)
    context={
        "service": service
    }
    return render(request,'menage/menage.html',context)