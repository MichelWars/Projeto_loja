from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render

from .forms import CustomUserCreationForm


# view para registro de usuarios
def register_view(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
    else:
        user_form = CustomUserCreationForm()

    return render(request, 'register.html', {'user_form': user_form})


# view para login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('catalogo')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
            login_form = AuthenticationForm(
                request
            )  # mantém dados preenchidos no form
    else:
        login_form = AuthenticationForm()

    return render(request, 'login.html', {'login_form': login_form})


# view para logout
def logout_view(request):
    logout(request)
    return redirect('catalogo')
