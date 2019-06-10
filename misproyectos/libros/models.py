from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils import Choices
from django.core.exceptions import ValidationError
import datetime, uuid

class Autores(models.Model):
    nombre = models.CharField(   
        verbose_name="Nombre de autor",
        max_length=50,
        help_text=_('Nombre de autor'),
    ) 
    class Meta:
        verbose_name = _('Autor')
        verbose_name_plural = _('Lista de autores')
        db_table='Autores'
        app_label= 'libros'

    def __str__(self):
        return self.nombre.title()

class Generos(models.Model):
    genero = models.CharField(   
        verbose_name="Genero literiario",
        max_length=50,
        help_text=_('Digite genero literario'),
    ) 

    class Meta:
        verbose_name = _('Genero')
        verbose_name_plural = _('Lista de generos')
        db_table='Generos'
        app_label= 'libros'

    def __str__(self):
        return self.genero.title()

class Ubicacion(models.Model):
    ubicacion = models.CharField(   
        verbose_name="Ubicacion del libro",
        max_length=50,
        help_text=_('Digite genero literario'),
    ) 
    comentarios = models.TextField(   
        verbose_name="Comentarios sobre la ubicacion",
        help_text=_('Digite comentarios sobre sobre la ubicacion'),
    ) 

    class Meta:
        verbose_name = _('Ubicacion')
        verbose_name_plural = _('Lista de ubicaciones')
        db_table='Ubicacion'
        app_label= 'libros'

    def __str__(self):
        return self.ubicacion.title()

class Libros(models.Model):
    titulo = models.CharField(   
        verbose_name="Titulo del libro",
        max_length=50,
        help_text=_('Digite el titulo del libro'),
    ) 
    autor = models.ForeignKey(
        Autores,
        on_delete=models.CASCADE,
        related_name='libro_autor',
        verbose_name='Autor',             
        help_text=_('Seleccione autor'),
    )
    genero = models.ForeignKey(
        Generos,
        on_delete=models.CASCADE,
        related_name='genero_autor',
        verbose_name='Genero',             
        help_text=_('Seleccione genero'),
    )
    ubicacion = models.ForeignKey(
        Ubicacion,
        on_delete=models.CASCADE,
        related_name='libro_ubicacion',
        verbose_name='Ubicacion',             
        help_text=_('Seleccione ubicacion'),
    )
    fecha_compra =  models.DateTimeField(
        verbose_name='Fecha de compra',
        help_text=_('Digite fecha de compra'),
    )
    sinapsis = models.TextField(   
        verbose_name="Sinapsis del libro",
        help_text=_('Digite sinapsis del libro'),
    ) 
    comentarios = models.TextField(   
        verbose_name="Comentarios sobre el libro",
        help_text=_('Digite comentarios sobre el libro'),
    ) 

    class Meta:
        verbose_name = _('Libro')
        verbose_name_plural = _('Lista de libros')
        db_table='Libros'
        app_label= 'libros'

    def __str__(self):
        return self.titulo.title()







