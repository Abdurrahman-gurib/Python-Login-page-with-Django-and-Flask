from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import User

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.filter(username=username, password=password).first()
            if user:
                # User authenticated, redirect to a success page
                return redirect('success')
            else:
                # Invalid credentials, display an error message
                error_message = "Invalid username or password."
    else:
        form = LoginForm()
        error_message = None
    return render(request, 'login.html', {'form': form, 'error_message': error_message})

def success(request):
    return render(request, 'success.html')
