from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .forms import UserForm


# Create your views here.
def login(request):
    content = {}
    return render(request, "loginForm.html", content)

def registration(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        
        if form.is_valid():
            sign_up = form.save(commit=False)
            sign_up.password = make_password(form.cleaned_data['password'])
            sign_up.save()
            return redirect('login')
    context = {'form':form}
    return render(request, "registrationForm.html",context)