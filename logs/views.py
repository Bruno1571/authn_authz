from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post 


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

    return render(request, "registration/register.html", {"form": form})  # Renderiza la plantilla con el formulario


@login_required
def posts_create(request):
    if request.method == 'POST':
        title = request.POST['Titulo']
        content = request.POST['Contenido']
        post = Post(Titulo=title, Contenido=content, Autor=request.user)
        post.save()
        return redirect('home')  
    return render(request, 'create.html')

@login_required
def home(request):
    nombreAutor = request.GET.get('autor')
    if nombreAutor:
        user = User.objects.filter(username=nombreAutor).first()
        if user:
            posts = Post.objects.filter(Autor=user)
        else:
            posts = []
    else:
        posts = Post.objects.all()

    return render(request, 'home.html', {'posts': posts, 'nombreAutor': nombreAutor})

@login_required
def posts_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('home')

    return render(request, 'confirmar_eliminacion.html', {'post': post})

@login_required
def posts_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.Titulo = request.POST.get('Titulo')  
        post.Contenido = request.POST.get('Contenido') 
        post.save()
        return redirect('home')

    return render(request, 'editarPublicacion.html', {'post': post})


@login_required
def posts_detail(request, post_id):
    # Recupera el post usando el ID proporcionado. Si no se encuentra, se muestra un error 404.
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'detallePublicaciones.html', {'post': post})

