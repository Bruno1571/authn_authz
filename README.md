# Proyecto de Autorización y Autenticación
Es una aplicación simple para verificar cómo funciona el sistema de autorización y autenticación en Django.
Hace uso del modelo de usuario proporcionado por defecto para registrar usuarios, los cuales se les asignan roles como "Administrador", "Editor" y "Creador". 
Estos roles cuentan con permisos específicos para cada grupo, como `add_task`, `change_task`, `delete_task`, entre otros.

## Instalación
1. Clonar el repositorio.
   Utilizando el link, puede clonarse desde Visual Studio Code y colocarse en la carpeta de preferencia:
   Desde VSC, pulsar las teclas Control + Shift + P y luego seleccionar o escribir la opción que diga Git: Clone
   Una vez hecho esto, solo hay que copiar y pegar el enlace.
   https://github.com/Bruno1571/authn_authz.git
   
2. Crear y activar el entorno virtual.
   Dentro de la carpeta que se creará el Entorno Virtual se ejecuta el siguiente comando desde la terminal:
   python -m venv env
   Estando dentro de la carpeta, para activarlo hay que ejecutar:
   En Linux: source env/bin/activate
   En Windows: env\Scripts\activate

3. Instalar las dependencias.
   Para instalar las dependecias uno debe estar parado en la carpeta principal del proyecto, que es donde se encuentra el archivo requirements.txt
   Luego desde la consola de comandos:
   pip install -r requirements.txt

4. Aplicar las migraciones de la base de datos.
   El comando migrate aplicará las migraciones a la base de datos local, creando las tablas necesarias para que el proyecto funcione correctamente:
   python manage.py migrate

## Método de uso
  Para utiizar este programa, lo primero que hay que hacer es activar el proyecto mediante el comando python manage.py runserver.
  Esto hará que se ejecute en el navegador a través de la IP local: http://127.0.0.1:8000/
  También puede ser accederse directamente si se usa Control + Clic en el enlace que aparece al correr el servidor.
