from django.shortcuts import render, get_object_or_404, redirect

from menage.models import Menus, Services, Order

# Create your views here.

def index(request):
    menus=Menus.objects.all()
    context={
        "menus": menus
    }
    return render(request,'menage/index.html', context)

def detail(request, id):
    menu=get_object_or_404(Menus,id=id)
    services=Services.objects.filter(menu=menu)
    if menu.name=='immobilier':
        template='menage/detail_immobilier.html'
    else:
        template='menage/detail.html'
    context={
        "menu": menu,
        "services": services
    }
    return render(request,template, context)

def contact(request):
    return render(request, 'menage/contact.html')

def menage(request,id):
    service=get_object_or_404(Services,id=id)
    if service.menu.name=="immobilier":
        template='menage/immobilier.html'
    else:
        template='menage/menage.html'
        
    if request.method=='POST':
        user=request.user
        name=request.POST.get('name')
        email=request.POST.get('email')
        tel=request.POST.get('tel')
        adresse=request.POST.get('adresse')
        if 'particulier' in request.POST:
            types=('particulier')
        if 'entreprise' in request.POST:
            types=('entreprise')
        # Order.objects.create(types=types,user=user,service=service,phone=tel,adresse=adresse)
        context={
            'name':name,
            'email':email,
            'tel':tel,
            'adresse':adresse,
        }
        return render(request,'menage/soumettre.html', context)
    context={
        "service": service
    }
    return render(request,template,context)