from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Categoria, Proveedor, Producto
from .forms import CategoriaForm, ProveedorForm, ProductoForm


def lista_categorias(request):
    categorias = Categoria.objects.all()

    return render(
        request,
        'categoria/lista.html',
        {'categorias': categorias}
    )


def lista_proveedores(request):
    proveedores = Proveedor.objects.all()

    return render(
        request,
        'proveedor/lista.html',
        {'proveedores': proveedores}
    )


@login_required
def crear_proveedor(request):

    if request.method == 'POST':
        form = ProveedorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')

    else:
        form = ProveedorForm()

    return render(
        request,
        'proveedor/form.html',
        {'form': form}
    )


@login_required
def editar_proveedor(request, pk):

    proveedor = get_object_or_404(
        Proveedor,
        pk=pk
    )

    if request.method == 'POST':

        form = ProveedorForm(
            request.POST,
            instance=proveedor
        )

        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')

    else:

        form = ProveedorForm(
            instance=proveedor
        )

    return render(
        request,
        'proveedor/form.html',
        {'form': form}
    )


def eliminar_proveedor(request, pk):

    if not request.user.is_authenticated:
        return redirect('login')

    if not request.user.is_staff:
        raise PermissionDenied

    proveedor = get_object_or_404(
        Proveedor,
        pk=pk
    )

    if request.method == 'POST':
        proveedor.delete()
        return redirect('lista_proveedores')

    return render(
        request,
        'confirm_delete.html',
        {
            'titulo': 'Eliminar proveedor',
            'objeto': proveedor,
            'cancelar_url': reverse('lista_proveedores'),
        }
    )


def lista_productos(request):
    productos = Producto.objects.select_related('categoria', 'proveedor').all()

    return render(
        request,
        'producto/lista.html',
        {'productos': productos}
    )


@login_required
def crear_producto(request):

    if request.method == 'POST':
        form = ProductoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_productos')

    else:
        form = ProductoForm()

    return render(
        request,
        'producto/form.html',
        {'form': form}
    )


@login_required
def editar_producto(request, pk):

    producto = get_object_or_404(
        Producto,
        pk=pk
    )

    if request.method == 'POST':

        form = ProductoForm(
            request.POST,
            instance=producto
        )

        if form.is_valid():
            form.save()
            return redirect('lista_productos')

    else:

        form = ProductoForm(
            instance=producto
        )

    return render(
        request,
        'producto/form.html',
        {'form': form}
    )


def eliminar_producto(request, pk):

    if not request.user.is_authenticated:
        return redirect('login')

    if not request.user.is_staff:
        raise PermissionDenied

    producto = get_object_or_404(
        Producto,
        pk=pk
    )

    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')

    return render(
        request,
        'confirm_delete.html',
        {
            'titulo': 'Eliminar producto',
            'objeto': producto,
            'cancelar_url': reverse('lista_productos'),
        }
    )


@login_required
def crear_categoria(request):

    if request.method == 'POST':
        form = CategoriaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_categorias')

    else:
        form = CategoriaForm()

    return render(
        request,
        'categoria/form.html',
        {'form': form}
    )


@login_required
def editar_categoria(request, pk):

    categoria = get_object_or_404(
        Categoria,
        pk=pk
    )

    if request.method == 'POST':

        form = CategoriaForm(
            request.POST,
            instance=categoria
        )

        if form.is_valid():
            form.save()
            return redirect('lista_categorias')

    else:

        form = CategoriaForm(
            instance=categoria
        )

    return render(
        request,
        'categoria/form.html',
        {'form': form}
    )


def eliminar_categoria(request, pk):

    if not request.user.is_authenticated:
        return redirect('login')

    if not request.user.is_staff:
        raise PermissionDenied

    categoria = get_object_or_404(
        Categoria,
        pk=pk
    )

    if request.method == 'POST':
        categoria.delete()
        return redirect('lista_categorias')

    return render(
        request,
        'confirm_delete.html',
        {
            'titulo': 'Eliminar categoría',
            'objeto': categoria,
            'cancelar_url': reverse('lista_categorias'),
        }
    )