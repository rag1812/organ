# recipient/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RecipientForm
from donor.models import Donor
from .models import Recipient
from django.contrib.auth.decorators import login_required

@login_required
def recipient_form(request):
    if request.method == "POST":
        form = RecipientForm(request.POST)
        if form.is_valid():
            recipient = form.save(commit=False)
            recipient.user = request.user
            recipient.save()

            # Match recipient details with donor details
            matching_donors = Donor.objects.filter(
                organ=recipient.organ_needed,
                blood_group=recipient.blood_group,
                willing_to_donate=True
            )

            if matching_donors.exists():
                return render(
                    request,
                    'recipient/match_found.html',
                    {'donors': matching_donors, 'recipient': recipient}
                )
            else:
                return render(
                    request,
                    'recipient/no_match.html',
                    {'recipient': recipient}
                )
    else:
        form = RecipientForm()

    return render(request, 'recipient/recipient_form.html', {'form': form})

@login_required
def send_request_to_admin(request, recipient_id, donor_id):
    try:
        recipient_obj = get_object_or_404(Recipient, id=recipient_id)
        donor_obj = get_object_or_404(Donor, id=donor_id)

        # Mark the request as sent
        recipient_obj.is_request_sent = True
        recipient_obj.save()

        # Notify admin or take further action
        return render(
            request,
            'recipient/request_sent.html',
            {'recipient': recipient_obj, 'donor': donor_obj}
        )
    except Recipient.DoesNotExist:
        return render(request, 'recipient/error.html', {'error_message': 'Recipient not found'})
    except Donor.DoesNotExist:
        return render(request, 'recipient/error.html', {'error_message': 'Donor not found'})
