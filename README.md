# 🎓 Sistema de Gestión Escolar

Aplicación web desarrollada con **Django** para la administración básica de una institución educativa.
El sistema permite gestionar **alumnos, profesores y cursos**, incluyendo relaciones entre ellos.

Este proyecto fue desarrollado como práctica del programa **Desarrollo de Aplicaciones Full Stack con Python**, aplicando la arquitectura **MVC de Django** y diseño moderno utilizando **TailwindCSS**.

---

# 📚 Funcionalidades

El sistema incluye gestión completa de las siguientes entidades:

## 👨‍🎓 Alumnos

* Crear alumno
* Editar información
* Ver detalle del alumno
* Eliminar alumno
* Listado completo de alumnos

## 👨‍🏫 Profesores

* Crear profesor
* Editar profesor
* Ver detalle
* Eliminar profesor
* Listado de profesores

## 📖 Cursos

* Crear curso
* Asignar profesor a un curso
* Inscribir alumnos en un curso
* Editar curso
* Eliminar curso
* Visualizar alumnos inscritos

## 🔐 Autenticación

* Inicio de sesión con sistema de autenticación de Django
* Protección de vistas mediante usuarios autenticados

---

# 🧱 Estructura del Proyecto

App_Gestion_Escolar/
│
├── alumnos/           # CRUD de alumnos
├── profesores/        # CRUD de profesores
├── cursos/            # Gestión de cursos
│
├── templates/         # Plantillas HTML del sistema
├── static/            # Archivos CSS, JS e imágenes
│
├── gestion_escolar/   # Configuración principal del proyecto
│
├── db.sqlite3
├── manage.py
└── requirements.txt

---

# 🛠️ Tecnologías utilizadas

* Python 3
* Django
* SQLite
* HTML5
* TailwindCSS
* Material Symbols (Google Icons)
* Git & GitHub

---

# 🎨 Interfaz

La interfaz fue desarrollada con **TailwindCSS**, permitiendo una apariencia moderna y adaptable a distintos dispositivos.

Características principales de la interfaz:

* Formularios estilizados
* Iconografía Material Design
* Diseño consistente en todas las vistas
* Componentes reutilizables
* Interfaz responsive

---

# 🚀 Instalación y ejecución

## 1️⃣ Clonar el repositorio

git clone https://github.com/veragonzalo/App_Gestion_Escolar.git

## 2️⃣ Entrar al proyecto

cd App_Gestion_Escolar

## 3️⃣ Crear entorno virtual

python -m venv venv

### Activar entorno virtual

Windows

venv\Scripts\activate

Linux / Mac

source venv/bin/activate

---

## 4️⃣ Instalar dependencias

pip install -r requirements.txt

---

## 5️⃣ Ejecutar migraciones

python manage.py makemigrations
python manage.py migrate

---

## 6️⃣ Crear superusuario

python manage.py createsuperuser

---

## 7️⃣ Ejecutar servidor

python manage.py runserver

Abrir en el navegador:

http://127.0.0.1:8000

---

# 🔑 Acceso al sistema

Inicio de sesión:

http://127.0.0.1:8000/login/

Panel administrativo de Django:

http://127.0.0.1:8000/admin/

---

# 📸 Módulos del sistema

| Módulo     | Descripción                         |
| ---------- | ----------------------------------- |
| Alumnos    | Registro y gestión de estudiantes   |
| Profesores | Administración del personal docente |
| Cursos     | Asignación de profesores y alumnos  |

---

# 📈 Mejoras futuras

Algunas mejoras que pueden incorporarse al sistema:

* Dashboard con estadísticas
* Buscador y filtros avanzados
* Sistema de calificaciones
* Exportación de reportes
* API REST con Django Rest Framework
* Gestión de usuarios con roles

---

# 👨‍💻 Autor

**Gonzalo Vera Cerda**

📍 Puerto Montt, Chile
📧 [gonzalo.vera.cerda@gmail.com](mailto:gonzalo.vera.cerda@gmail.com)

LinkedIn
https://www.linkedin.com/

---

# 📄 Licencia

Este proyecto se distribuye bajo licencia **MIT**.
