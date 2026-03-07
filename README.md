# 🎓 Sistema de Gestión Escolar - Liceo Digital

![Django](https://img.shields.io/badge/Django-6.0-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/Tailwind-3.0-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

Sistema integral de gestión escolar desarrollado con Django, diseñado para administrar alumnos, profesores y cursos en instituciones educativas.

---

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Capturas de Pantalla](#-capturas-de-pantalla)
- [Tecnologías](#-tecnologías)
- [Requisitos](#-requisitos)
- [Instalación](#-instalación)
- [Configuración](#-configuración)
- [Uso](#-uso)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Contribuir](#-contribuir)
- [Licencia](#-licencia)
- [Contacto](#-contacto)

---

## ✨ Características

### 🎯 Módulos Principales

#### 👨‍🎓 Gestión de Alumnos
- ✅ Registro completo de estudiantes con validación
- ✅ Listado con búsqueda y filtros
- ✅ Fichas personales con datos académicos
- ✅ Sistema de edad automático

#### 👨‍🏫 Gestión de Profesores
- ✅ Directorio de personal docente
- ✅ Registro con datos profesionales
- ✅ Validación de fecha de nacimiento (formato DD-MM-AAAA)
- ✅ Control de especialidades

#### 📚 Gestión de Cursos
- ✅ Catálogo de cursos académicos
- ✅ Planificación curricular
- ✅ Asignación de materias

### 🔐 Sistema de Autenticación
- ✅ Login personalizado con diseño corporativo
- ✅ Logout con página de confirmación
- ✅ Control de sesiones
- ✅ Permisos basados en roles (Superusuario, Administrador, Usuario)

### 🎨 Panel de Administración
- ✅ Django Admin completamente personalizado
- ✅ Tema corporativo con colores institucionales (#002147)
- ✅ Interfaz moderna y responsive
- ✅ Dashboard con estadísticas (en desarrollo)

### 📱 Diseño Responsivo
- ✅ Compatible con dispositivos móviles, tablets y desktop
- ✅ Diseño adaptativo usando Tailwind CSS
- ✅ Iconos Material Symbols
- ✅ Efectos hover y transiciones suaves

---

## 📸 Capturas de Pantalla

### Portal Principal
![Portal Principal](https://via.placeholder.com/800x400/002147/FFFFFF?text=Portal+Principal)

### Panel de Administración
![Admin Panel](https://via.placeholder.com/800x400/002147/FFFFFF?text=Panel+Admin)

### Gestión de Alumnos
![Gestión Alumnos](https://via.placeholder.com/800x400/002147/FFFFFF?text=Gestion+Alumnos)

---

## 🛠 Tecnologías

### Backend
- **Django 6.0.2** - Framework web de Python
- **Python 3.13** - Lenguaje de programación
- **SQLite** - Base de datos (desarrollo)

### Frontend
- **HTML5** - Estructura
- **Tailwind CSS 3.0** - Framework CSS
- **JavaScript (Vanilla)** - Interactividad
- **Material Symbols** - Iconografía
- **Flatpickr** - Selector de fechas

### Herramientas
- **PyCharm** - IDE
- **Git** - Control de versiones
- **GitHub** - Repositorio remoto

---

## 📦 Requisitos

### Software necesario:
- Python 3.13 o superior
- pip (gestor de paquetes de Python)
- Git

### Dependencias del proyecto:
```txt
Django==6.0.2
```

---

## 🚀 Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/veragonzalo/App_Gestion_Escolar.git
cd App_Gestion_Escolar
```

### 2. Crear entorno virtual

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Realizar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crear superusuario
```bash
python manage.py createsuperuser
```

Sigue las instrucciones para crear tu cuenta de administrador.

### 6. Ejecutar el servidor de desarrollo
```bash
python manage.py runserver
```

Abre tu navegador en: **http://127.0.0.1:8000/**

---

## ⚙️ Configuración

### Variables de Entorno (Producción)

Crea un archivo `.env` en la raíz del proyecto:
```env
SECRET_KEY=tu-clave-secreta-aqui
DEBUG=False
ALLOWED_HOSTS=tudominio.com,www.tudominio.com
DATABASE_URL=postgresql://usuario:password@localhost/nombre_db
```

### Configuración de Base de Datos

Por defecto usa SQLite. Para producción, configura PostgreSQL en `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_bd',
        'USER': 'usuario',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## 💻 Uso

### Acceso al Sistema

1. **Portal Principal**: http://127.0.0.1:8000/
2. **Panel de Administración**: http://127.0.0.1:8000/admin/
3. **Login**: http://127.0.0.1:8000/login/

### Credenciales de Prueba

Usa las credenciales del superusuario que creaste durante la instalación.

### Navegación

- **Inicio** - Portal principal con acceso a todos los módulos
- **Alumnos** - Gestión de estudiantes
- **Profesores** - Directorio de docentes
- **Cursos** - Catálogo de cursos académicos
- **Admin** - Panel de administración de Django

---

## 📁 Estructura del Proyecto
```
App_Gestion_Escolar/
│
├── App_Gestion_Escolar/      # Configuración principal del proyecto
│   ├── settings.py            # Configuración de Django
│   ├── urls.py                # URLs principales
│   ├── views.py               # Vistas generales
│   └── wsgi.py                # Configuración WSGI
│
├── alumnos/                   # App de Alumnos
│   ├── migrations/            # Migraciones de BD
│   ├── templates/             # Templates de alumnos
│   ├── forms.py               # Formularios
│   ├── models.py              # Modelos de datos
│   ├── urls.py                # URLs de alumnos
│   └── views.py               # Vistas de alumnos
│
├── profesores/                # App de Profesores
│   ├── migrations/
│   ├── templates/
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── cursos/                    # App de Cursos
│   ├── migrations/
│   ├── templates/
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── templates/                 # Templates globales
│   ├── admin/                 # Templates del admin personalizados
│   │   ├── base_site.html     # Header del admin
│   │   └── logged_out.html    # Página de logout
│   ├── registration/
│   │   └── logged_out.html    # Logout de apps
│   ├── base.html              # Template base
│   └── login.html             # Página de login
│
├── static/                    # Archivos estáticos
│   ├── css/
│   │   └── estilos.css
│   └── js/
│       └── scripts.js
│
├── db.sqlite3                 # Base de datos (desarrollo)
├── manage.py                  # Script de gestión de Django
└── requirements.txt           # Dependencias del proyecto
```

---

## 🤝 Contribuir

Las contribuciones son bienvenidas. Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add: nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

### Convenciones de Commits

- `Add:` Nueva funcionalidad
- `Fix:` Corrección de bugs
- `Update:` Actualización de código existente
- `Docs:` Cambios en documentación
- `Style:` Cambios de formato/estilo

---

## 📝 Roadmap

### Próximas Funcionalidades

- [ ] Dashboard con estadísticas y gráficos
- [ ] Sistema de calificaciones
- [ ] Control de asistencia
- [ ] Generación de reportes PDF
- [ ] Exportación de datos a Excel
- [ ] Sistema de notificaciones
- [ ] API REST con Django REST Framework
- [ ] Aplicación móvil (React Native)
- [ ] Sistema de mensajería interna
- [ ] Integración con Google Classroom

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

## 👤 Autor

**Gonzalo Vera**

- GitHub: [@veragonzalo](https://github.com/veragonzalo)
- Proyecto: [App_Gestion_Escolar](https://github.com/veragonzalo/App_Gestion_Escolar)

---

## 🙏 Agradecimientos

- Django Documentation
- Tailwind CSS
- Material Symbols by Google
- Flatpickr
- Unsplash (imágenes)

---

## 📞 Soporte

Si encuentras algún problema o tienes alguna pregunta:

1. Abre un [Issue](https://github.com/veragonzalo/App_Gestion_Escolar/issues)
2. Contacta al autor

---

## 🌟 ¿Te gustó el proyecto?

Si este proyecto te fue útil, por favor considera:

- ⭐ Darle una estrella en GitHub
- 🍴 Hacer un Fork
- 📢 Compartirlo con otros

---

<div align="center">

**Hecho con ❤️ por Gonzalo Vera**

**© 2024 Liceo Digital - Sistema de Gestión Escolar**

</div>
