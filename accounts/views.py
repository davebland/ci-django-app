from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import LoginForm, NewUserRegistrationForm

# Create your views here.
def test_page(request):
    return HttpResponse("Accounts Test View")
    
def index(request):
    return render(request, 'index.html')
    
@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect(reverse('index'))
    
def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                        password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "Successfully logged in")
                return redirect(reverse('index'))
            else:
                form.add_error(None, "Incorrect Login")
    else:
        form = LoginForm()
    return render(request, 'login.html', {"login_form":form})
    
def registration(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        registration_form = NewUserRegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "Registration successful")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Registration failed")
                return redirect(reverse('index'))
    else:
        registration_form = NewUserRegistrationForm()
    return render(request, 'registration.html', {'registration_form':registration_form})
    
def user_profile(request):
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {'user_profile':user})