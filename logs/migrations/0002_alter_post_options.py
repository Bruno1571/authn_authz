# Generated by Django 4.2 on 2024-11-04 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': [('crear_publicacion', 'Puede crear publicaciones'), ('editar_publicacion', 'Puede editar publicaciones'), ('eliminar_publicacion', 'Puede eliminar publicaciones'), ('ver_publicacion', 'Puede ver publicaciones')]},
        ),
    ]
