from django.urls import path
from . import views

urlpatterns = [

    # Categorías
    path(
        'categorias/',
        views.lista_categorias,
        name='lista_categorias'
    ),
    path(
        'categorias/nuevo/',
        views.crear_categoria,
        name='crear_categoria'
    ),
    path(
        'categorias/editar/<int:pk>/',
        views.editar_categoria,
        name='editar_categoria'
    ),
    path(
        'categorias/eliminar/<int:pk>/',
        views.eliminar_categoria,
        name='eliminar_categoria'
    ),

    # Proveedores
    path(
        'proveedores/',
        views.lista_proveedores,
        name='lista_proveedores'
    ),
    path(
        'proveedores/nuevo/',
        views.crear_proveedor,
        name='crear_proveedor'
    ),
    path(
        'proveedores/editar/<int:pk>/',
        views.editar_proveedor,
        name='editar_proveedor'
    ),
    path(
        'proveedores/eliminar/<int:pk>/',
        views.eliminar_proveedor,
        name='eliminar_proveedor'
    ),

    # Productos
    path(
        'productos/',
        views.lista_productos,
        name='lista_productos'
    ),

    path(
        'productos/nuevo/',
        views.crear_producto,
        name='crear_producto'
    ),

    path(
        'productos/editar/<int:pk>/',
        views.editar_producto,
        name='editar_producto'
    ),

    path(
        'productos/eliminar/<int:pk>/',
        views.eliminar_producto,
        name='eliminar_producto'
    ),
]