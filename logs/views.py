from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post 
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():  # Verifica si el formulario es válido
            user = form.save()  # Guarda el nuevo usuario y obtiene la instancia
            username = form.cleaned_data.get("username")
            messages.success(request, f"¡Cuenta creada para {username}!")  # Mensaje de éxito
            content_type = ContentType.objects.get(app_label='logs', model='post')
            permiso = Permission.objects.get(codename='view_post', content_type=content_type)
            user.user_permissions.add(permiso)  # Agrega el permiso al usuario

            return redirect("login")  # Redirecciona a la página de inicio de sesión
    else:
        form = UserCreationForm()  # Inicializa el formulario si la solicitud es GET

    return render(request, "registration/register.html", {"form": form})  # Renderiza la plantilla con el formulario


@login_required 
@permission_required('logs.add_post', raise_exception=True)
def posts_create(request):
    if request.method == 'POST':
        title = request.POST['Titulo']
        content = request.POST['Contenido']
        post = Post(Titulo=title, Contenido=content, Autor=request.user)
        post.save()
        return redirect('home')  
    return render(request, 'create.html')

@login_required
@permission_required('logs.view_post', raise_exception=True)
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
    can_create = request.user.has_perm('logs.add_post')
    return render(request, 'home.html', {'posts': posts, 'nombreAutor': nombreAutor, 'can_create': can_create})

@login_required
@permission_required('logs.delete_post', raise_exception=True)
def posts_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('home')

    return render(request, 'confirmar_eliminacion.html', {'post': post})

@login_required
@permission_required('logs.change_post', raise_exception=True)
def posts_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.Titulo = request.POST.get('Titulo')  
        post.Contenido = request.POST.get('Contenido') 
        post.save()
        return redirect('home')

    return render(request, 'editarPublicacion.html', {'post': post})


@login_required
@permission_required('logs.view_post', raise_exception=True)
def posts_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    can_delete = request.user.has_perm('logs.delete_post')
    can_edit = request.user.has_perm('logs.change_post')
    return render(request, 'detallePublicaciones.html', {'post': post, 'can_delete': can_delete, 'can_edit': can_edit})
