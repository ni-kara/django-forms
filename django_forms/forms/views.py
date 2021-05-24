from django.shortcuts import render, redirect
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
            form.save()
            return redirect('login')
    context = {'form':form}
    return render(request, "registrationForm.html",context)