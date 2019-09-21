from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import LoginForm

# Create your views here.
def test_page(request):
    return HttpResponse("Accounts Test View")
    
def index(request):
    return render(request, 'index.html')
    
def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect(reverse('index'))
    
def login(request):
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