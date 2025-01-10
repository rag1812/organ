from django.shortcuts import render


def home_view(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'login.html')  # Create a `login.html`

def signup_view(request):
    return render(request, 'signup.html')  # Create a `signup.html`

def profile_view(request):
    return render(request, 'profile.html')  

def donor_page(request):
    return render(request, 'accounts/donor.html')
 
def recipient_page(request):
    return render(request, 'accounts/recipient.html') 



