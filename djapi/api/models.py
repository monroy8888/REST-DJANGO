from django.db import models

<<<<<<< HEAD

=======
>>>>>>> d1ab9efe8581a19894795d50d0a00318bd16f9f1
class Categoria(models.Model):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Categoría',
        unique=True
        )
<<<<<<< HEAD

    def __str__(self):
        return '{}'.format(self.descripcion)

    class Meta:
        verbose_name_plural = "Categorías"


=======
        
    def __str__(self):
        return '{}'.format(self.descripcion)
        
    class Meta:
        verbose_name_plural = "Categorías"

>>>>>>> d1ab9efe8581a19894795d50d0a00318bd16f9f1
class SubCategoria(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Sub Categoría'
        )
<<<<<<< HEAD

    def __str__(self):
        return '{}:{}'.format(self.categoria.descripcion, self.descripcion)

    class Meta:
        verbose_name_plural = "Sub Categorías"
        unique_together = ('categoria', 'descripcion')


=======
        
    def __str__(self):
        return '{}:{}'.format(self.categoria.descripcion,self.descripcion)
    
    class Meta:
        verbose_name_plural = "Sub Categorías"
        unique_together = ('categoria','descripcion')
     
     
>>>>>>> d1ab9efe8581a19894795d50d0a00318bd16f9f1
class Producto(models.Model):
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción del Producto',
        unique=True
        )
<<<<<<< HEAD
    fecha_creado = models.DateTimeField()
    vendido = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.descripcion)

=======
        fecha_creado = models.DateTimeField()
        vendido = models.BooleanField(default=False)
     
    def __str__(self):
        return '{}'.format(self.descripcion)
    
>>>>>>> d1ab9efe8581a19894795d50d0a00318bd16f9f1
    class Meta:
        verbose_name_plural = "Productos"
