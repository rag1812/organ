from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import DonorForm
from .models import Donor

@login_required
def new_donor(request):
    """
    Render the donor registration form.
    """
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            donor = form.save(commit=False)
            donor.user = request.user  # Associate the logged-in user
            donor.save()
            return redirect('donor_details')  # Redirect to donor details after successful submission
    else:
        form = DonorForm()

    return render(request, 'donor/new_donor.html', {'form': form})


def donor_redirect(request):
    """
    Redirect logic for donors:
    - If the user is a first-time donor, redirect to the registration form.
    - If the user has already donated, redirect to the details page.
    """
    if not request.user.is_authenticated:
        return redirect('login')  # Ensure the user is logged in before proceeding

    # Check if the user has already donated
    existing_donors = Donor.objects.filter(user=request.user)

    if existing_donors.exists():
        return redirect('donor_details')  # Redirect to donor details page
    else:
        return redirect('new_donor')  # Redirect to donor registration form
    

def donor_details(request):
    
    if not request.user.is_authenticated:
        return redirect('login')  # Ensure the user is logged in

    # Fetch donor details for the logged-in user
    donors = Donor.objects.filter(user=request.user)

    if not donors.exists():
        return redirect('new_donor')  # Redirect if no donor record exists

    context = {
        'donors': donors,
    }
    return render(request, 'donor/donor_details.html', context)