from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=100, verbose_name="Titulo")
    content=models.TextField(verbose_name="Contenido")
    image=models.ImageField(upload_to="products", verbose_name="Imagen")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")

    class Meta:
        verbose_name="producto"
        verbose_name_plural="productos"
        ordering=['-created']

    def __str__(self):
        return self.title