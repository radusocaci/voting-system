from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import UserRegisterForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
