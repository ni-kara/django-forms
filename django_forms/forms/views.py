from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User


# Create your views here.
def login(request):    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user is not None:   
            auth.login(request, user)             
            return redirect('/dashboard')
        else:
            print("Login failed")  
            messages.info(request, 'invalid credentials')              
            return redirect('/login', messages=messages) 
    
    content = {}
    return render(request, "loginForm.html", content)

def registration(request):    
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if User.objects.get(username=username):
            messages.info(request, 'This username exist')            
            return redirect('/', messages= messages)
        else:
            user = User.objects.create(username=username, email=email, password=password)
            user.save()        
            redirect("/login")     
 
    context = {}
    return render(request, "registrationForm.html",context)

def dashboard(request):
    content = {}
    return render(request, "dashboard.html", content)