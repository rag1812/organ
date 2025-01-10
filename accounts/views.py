from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import os
from django.conf import settings


def home(request):
    return render(request, 'home.html')


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
 
    # Render the login page with the new design
    return render(request, 'accounts/login.html', {'form': form})



BASE_DIR = settings.BASE_DIR

@login_required
def donor_page(request):
    # Debugging snippet to check if the template file exists
    template_path = os.path.join(BASE_DIR, 'templates/accounts/donor.html')
    print("Template path:", template_path)  # Print the full template path
    print("Does the template exist?", os.path.exists(template_path))  # Check if the file exists

    # Render the donor page template
    return render(request, 'accounts/donor.html')


def logout_view(request):
    logout(request)
    return redirect('home')

@login_required # type: ignore
def profile_view(request):
    return render(request, 'accounts/profile.html')

@login_required 
def donor_page(request):
    return render(request, 'donor.html') 
 
@login_required 
def recipient_page(request):
    return render(request, 'accounts/recipient.html')  