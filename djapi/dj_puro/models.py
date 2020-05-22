from django.db import models

class Categoria(models.Model):
    descripcion=models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return '{}'.format(self.descripcion)
    
    class Meta:
        verbose_name_plural = "Categorias"
