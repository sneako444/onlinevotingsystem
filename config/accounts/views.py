from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm  
from django.contrib.auth.decorators import login_required

User = get_user_model()  # Get the custom user model

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Create the user instance
            user.set_password(form.cleaned_data["password1"])  # Set password properly
            user.save()  # Now save the user
            login(request, user)
            return redirect("dashboard")  
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("dashboard")  # Change this to your homepage view
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})

@login_required
def dashboard_view(request):
    return render(request, "accounts/dashboard.html")
