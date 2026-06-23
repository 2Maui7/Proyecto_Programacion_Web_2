# Sistema de Inventario

Proyecto Django para gestionar categorías, proveedores y productos.

## Requisitos

- Python 3.14 o superior
- Django 5.2.8

## Instalación

1. Crear y activar un entorno virtual:

```bash
python -m venv venv
venv\Scripts\activate
```

2. Instalar las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

3. Aplicar migraciones:

```bash
python manage.py migrate
```

4. Crear un superusuario, si lo necesitas:

```bash
python manage.py createsuperuser
```

## Ejecutar el proyecto

```bash
python manage.py runserver
```

Luego abre en el navegador:

```bash
http://127.0.0.1:8000/
```

## Credenciales

Si ya existe un usuario en la base de datos, puedes iniciar sesión con sus credenciales creadas desde el admin o con `createsuperuser`.

