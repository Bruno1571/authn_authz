from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():  # Verifica si el formulario es válido
            form.save()  # Guarda el nuevo usuario
            username = form.cleaned_data.get("username")
            messages.success(request, f"¡Cuenta creada para {username}!")  # Mensaje de éxito
            return redirect("login")  # Redirecciona a la página de inicio de sesión
    else:
        form = UserCreationForm()  # Inicializa el formulario si la solicitud es GET

    return render(request, "register.html", {"form": form})  # Renderiza la plantilla con el formulario
