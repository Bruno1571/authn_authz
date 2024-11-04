from email.headerregistry import Group
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login 
from .models import Post 
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"¡Cuenta creada para {username}!")

            grupo = Group.objects.get(name='Lector')  
            user.groups.add(grupo) 

            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {"form": form})

@login_required 
@permission_required('logs.crear_publicacion', raise_exception=True)
def posts_create(request):
    if request.method == 'POST':
        title = request.POST['Titulo']
        content = request.POST['Contenido']
        post = Post(Titulo=title, Contenido=content, Autor=request.user)
        post.save()
        return redirect('home')  
    return render(request, 'create.html')

@login_required
@permission_required('logs.ver_publicacion', raise_exception=True)
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
    can_create = request.user.has_perm('logs.crear_publicacion')
    return render(request, 'home.html', {'posts': posts, 'nombreAutor': nombreAutor, 'can_create': can_create})

@login_required
@permission_required('logs.eliminar_publicacion', raise_exception=True)
def posts_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('home')

    return render(request, 'confirmar_eliminacion.html', {'post': post})

@login_required
@permission_required('logs.editar_publicacion', raise_exception=True)
def posts_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.Titulo = request.POST.get('Titulo')  
        post.Contenido = request.POST.get('Contenido') 
        post.save()
        return redirect('home')

    return render(request, 'editarPublicacion.html', {'post': post})

@login_required
@permission_required('logs.ver_publicacion', raise_exception=True)
def posts_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    can_delete = request.user.has_perm('logs.eliminar_publicacion')
    can_edit = request.user.has_perm('logs.editar_publicacion')
    return render(request, 'detallePublicaciones.html', {'post': post, 'can_delete': can_delete, 'can_edit': can_edit})
