# Proyecto de Autorización y Autenticación
Es una aplicación simple para verificar cómo funciona el sistema de autorización y autenticación en Django.
Hace uso del modelo de usuario proporcionado por defecto para registrar usuarios, los cuales se les asignan roles como "Administrador", "Editor", "Creador" y "Lector". 
Estos roles cuentan con permisos específicos para cada grupo, como `agregar_publicacion`, `editar_publicacion`, `eliminar_publicacion` y `ver_publicacion`.

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
1. Activar y entrar al servidor. 
  Para utiizar este programa, lo primero que hay que hacer es activar el proyecto mediante el comando python manage.py runserver.
  Esto hará que se ejecute en el navegador a través de la IP local: http://127.0.0.1:8000/
  También puede accederse directamente si se usa Control + Clic en el enlace que aparece al correr el servidor.

2. Registrarse e iniciar sesión.
   Una vez se accede a la aplicación, hay que registrarse o iniciar sesión con un usuario ya existente, así que se debe completar con los datos solicitados según corresponda.
   Para comprobar funcionalidades, hay usuarios previamente hechos con roles y permisos.
   Usuario: Administrador Contraseña: cincuenta
   Usuario: Editor Contraseña: cincuenta
   Usuario: Creador Contraseña: cincuenta

4. Usar funcionalidades.
   Se pueden crear tareas con descripciones, editar la descripción/título de las mismas o borrarlas desde la propia interfaz de la app al hacer clic en los botones correspondientes. 
   Funciones según el rol:
   Administrador: Tiene todas las funciones sobre todos los post.
   Editor: Tiene solo la función de `cambiar_publicacion` de todos los post.
   Creador: Únicamente tiene la función de `agregar_publicacion`. 
   Lector/Usuario registrado: Solo cuenta con `ver_publicacion` por lo que nomás puede ver los posts, sin poder crear ni editar.
   Se realizó de este modo para que cada uno de los roles tuviera una función y así comprobar cómo se ocultan/muestran las mismas según el usuario que acceda.

## Backend
Para este proyecto se utilizó el Backend de Base de Datos que viene por defecto al crear un proyecto en Django, el cual almacena las sesiones en una tabla llamada django_session. Este mismo es adecuado para la mayoría de los proyectos en sus primeras etapas y es una opción segura para la mayoría de los entornos de desarrollo y producción.
Se optó por este tipo de Backend teniendo en cuenta que es una aplicación simple que está en la etapa de desarrollo, no habrá más de un usuario concurrente a la vez, no presenta problemas de rendimiento y no se pleanea que escale, por lo que resulta la mejor opción frente a las demás. Al ser usado por un solo usuario a la vez y que existan pocos registros no hace falta el Backend de Caché, se descarta el cached_db por la complejitud innecesaria y un backend de archivos no es recomendable ni preciso para esta situación.

## Seguridad
La protección CSRF (Cross-Site Request Forgery) es una medida de seguridad que ayuda a prevenir que un sitio web malicioso realice solicitudes en nombre de un usuario autenticado sin su consentimiento. Django implementa un sistema de protección CSRF que incluye un token (csrf_token) para cada solicitud POST que realiza el usuario, el cual debe validarse en el servidor.
Django genera automáticamente un token CSRF único para cada sesión de usuario. Este token se almacena en una cookie en el navegador y se utiliza en formularios y solicitudes POST.
Debe incluirse en todos los formularios HTML que envíen datos al servidor mediante el método POST mediante el uso de la etiqueta {% csrf_token %} dentro del formulario en las plantillas.
Cuando el formulario se envía, se comprueba que el token enviado en el formulario coincida con el token almacenado en la cookie del navegador. Si coinciden, la solicitud se considera legítima y se procesa; si no coinciden, Django devuelve un error 403 (Forbidden), bloqueando la solicitud.

Prueba de comprobación:
Si se omite {% csrf_token %} en el formulario, saldrá un error 403 cuando se envíe el formulario, indicando que Django bloqueó la solicitud porque no encontró el token CSRF.
