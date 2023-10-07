from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login,logout
from .forms import PatientRegistrationForm


def login_view(request):
    referring_url = request.META.get('HTTP_REFERER', '/')

    if request.user.is_authenticated:
        # Redirect authenticated users to the referring URL
        return redirect(referring_url)
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # Log the user in
            auth_login(request, form.get_user())
            # Redirect to the referring URL (or a default URL)
            return redirect('home')
    else:
        form = AuthenticationForm()
    
    # If there are errors, the form will contain error messages
    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')



def new_patient(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            # If the form is valid, save the patient data
            form.save()
            # Redirect to a success page or another appropriate URL
            return redirect('home')
        else:
            # If there are errors, render the form with errors
            context = {'form': form}
            return render(request, 'accounts/patient/new.html', context)
    else:
        # For GET requests, display an empty form
        form = PatientRegistrationForm()
        context = {'form': form}
        return render(request, 'accounts/patient/new.html', context)
