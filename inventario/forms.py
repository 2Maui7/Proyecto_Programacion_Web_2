from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Categoria, Proveedor, Producto


class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            if isinstance(field.widget, (forms.Select, forms.SelectMultiple)):
                css_class = 'form-select'
            elif isinstance(field.widget, forms.CheckboxInput):
                css_class = 'form-check-input'
            else:
                css_class = 'form-control'

            existing_classes = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f'{existing_classes} {css_class}'.strip()


class BootstrapAuthenticationForm(BootstrapFormMixin, AuthenticationForm):
    pass


class CategoriaForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']


class ProveedorForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'telefono', 'email']


class ProductoForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'categoria', 'proveedor']
