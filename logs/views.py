from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get("username")
        messages.success(request, f"¡Cuenta creada para {username}!")
        return redirect("login") # Redireccionar a la página de inicio de sesión o cualquier otra página que desee
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})
