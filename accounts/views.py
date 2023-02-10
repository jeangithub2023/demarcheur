from django.shortcuts import render, redirect
from accounts.forms import RegisterForm, ProfileForm
# Create your views here.

def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        profileForm=ProfileForm(request.POST)
        if form.is_valid() and profileForm.is_valid():
            user=form.save(commit=False)
            profile=profileForm.save(commit=False)
            profile.user=user
            user.save()
            profile.save()
            return redirect('accounts:login')
    else:
        form=RegisterForm()
        profileForm=ProfileForm()
    return render(request,'accounts/register.html',{'form':form,'profileForm':profileForm})