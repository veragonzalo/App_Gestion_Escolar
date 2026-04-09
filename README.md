# 🏫 App Gestión Escolar

> Proyecto del Bootcamp **Desarrollo de Aplicaciones Full Stack Python** — sistema web de gestión escolar construido con Django, Python y desplegado en producción con AlwaysData.

---

## 📋 Descripción

**App Gestión Escolar** es una aplicación web completa para la administración integral de una institución educativa. Permite gestionar alumnos, apoderados, profesores, cursos, horarios, asistencia, notas y comunicaciones desde un panel centralizado con autenticación de usuarios.

Desarrollada con Django siguiendo el patrón **MTV (Model-Template-View)**, con base de datos SQLite, interfaz responsiva con Tailwind CSS y exportación de reportes en PDF.

---

## 🚀 Características principales

- 👩‍🎓 **Gestión de alumnos** — registro, listado con búsqueda y paginación, perfil detallado
- 👨‍👩‍👧 **Gestión de apoderados** — registro y vinculación a estudiantes, búsqueda y paginación
- 👨‍🏫 **Gestión de profesores** — alta y administración del cuerpo docente, búsqueda y paginación
- 📚 **Gestión de cursos** — creación de cursos y administración de matrículas con exportación PDF
- 🗓️ **Horarios** — asignación de asignaturas y bloques horarios por curso
- ✅ **Asistencia** — registro de asistencia diaria con exportación a PDF
- 📝 **Notas** — registro y consulta de calificaciones con exportación a PDF
- 💬 **Comunicaciones** — mensajería interna entre usuarios del sistema
- 👤 **Usuarios** — autenticación, perfiles de usuario y control de acceso
- 🔍 **Búsqueda y paginación** — disponible en todos los módulos de listado

---

## 🗂️ Estructura del proyecto

```
App_Gestion_Escolar/
│
├── App_Gestion_Escolar/     # Configuración principal del proyecto Django
│   ├── settings.py          # Configuración global (BD, apps, estáticos, etc.)
│   ├── urls.py              # Enrutador URL principal
│   ├── wsgi.py              # Punto de entrada WSGI
│   └── asgi.py              # Punto de entrada ASGI
│
├── alumnos/                 # App: gestión de estudiantes
├── apoderados/              # App: gestión de apoderados / tutores
├── asistencia/              # App: registro de asistencia diaria
├── comunicaciones/          # App: mensajería interna entre usuarios
├── cursos/                  # App: cursos y matrículas
├── horarios/                # App: asignaturas y bloques horarios
├── notas/                   # App: registro de calificaciones
├── profesores/              # App: gestión del cuerpo docente
├── usuarios/                # App: autenticación y perfiles de usuario
│
├── templates/               # Plantillas HTML compartidas
├── static/                  # Archivos estáticos (CSS, JS, imágenes)
├── db.sqlite3               # Base de datos SQLite
├── manage.py                # CLI de administración de Django
├── requirements.txt         # Dependencias del proyecto
└── .gitignore
```

---

## 🛠️ Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| **Python 3** | Lenguaje principal del backend |
| **Django** | Framework web MTV |
| **SQLite** | Base de datos relacional embebida |
| **HTML5** | Plantillas y estructura de las vistas |
| **Tailwind CSS** | Estilos e interfaz responsiva |
| **JavaScript** | Interactividad en el frontend |
| **ReportLab / xhtml2pdf** | Generación de reportes en PDF |
| **AlwaysData** | Hosting y despliegue en producción |

---

## ▶️ Cómo ejecutar el proyecto en local

### 1. Clonar el repositorio

```bash
git clone https://github.com/veragonzalo/App_Gestion_Escolar.git
cd App_Gestion_Escolar
```

### 2. Crear y activar un entorno virtual

```bash
# Crear entorno virtual
python -m venv venv

# Activar en macOS/Linux
source venv/bin/activate

# Activar en Windows
venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones

```bash
python manage.py migrate
```

### 5. Crear superusuario (opcional)

```bash
python manage.py createsuperuser
```

### 6. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

### 7. Abrir en el navegador

```
http://127.0.0.1:8000/
```

---

## 🗃️ Módulos de la aplicación

| Módulo | App Django | Descripción |
|---|---|---|
| Alumnos | `alumnos/` | Registro y gestión de estudiantes |
| Apoderados | `apoderados/` | Gestión de apoderados y tutores |
| Profesores | `profesores/` | Gestión del cuerpo docente |
| Cursos | `cursos/` | Cursos y matrículas con exportación PDF |
| Horarios | `horarios/` | Asignaturas y bloques horarios |
| Asistencia | `asistencia/` | Registro de asistencia con exportación PDF |
| Notas | `notas/` | Calificaciones con exportación PDF |
| Comunicaciones | `comunicaciones/` | Mensajería interna |
| Usuarios | `usuarios/` | Autenticación y perfiles |

---

## 🌐 Demo en producción

El proyecto está desplegado y disponible en:

👉 **[https://gestioncolegio.alwaysdata.net](https://gestioncolegio.alwaysdata.net/login/?next=/)**

---

## 👩‍💻 Autora

**Vera Gonzalo**
- GitHub: [@veragonzalo](https://github.com/veragonzalo)

---

## 📚 Contexto académico

Proyecto desarrollado como parte del **Bootcamp Desarrollo de Aplicaciones Full Stack Python** — aplicando Django, patrón MTV, despliegue en producción y desarrollo incremental con múltiples módulos funcionales.

---

## 📄 Licencia

Este proyecto es de uso académico y educativo.
