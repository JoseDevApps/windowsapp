from django.db import models

class Tarea(models.Model):
    nombre = models.CharField(max_length = 200, blank=False, unique=True)
    inicio = models.DateTimeField(blank=True, null=True, default=None)
    repetir = models.CharField(max_length = 200, blank=True, unique=False)
    habilitar = models.BooleanField(blank=True, null=True, default=False)
    def __str__(self) -> str:
        return self.nombre

class Accion(models.Model):
    ACCIONES = (
        ('screen','screen'),
        ('move','move'),
        ('write_text','write_text'),
        ('push_enter','push_enter'),
        ('wait','wait')
    )

    nombre = models.CharField(max_length = 200, blank=False, unique=True)
    tareaID = models.ForeignKey(Tarea, on_delete = models.CASCADE)
    accion_model = models.CharField(max_length=200, null=True, choices=ACCIONES)
    imagen = models.ImageField(upload_to='screens/',blank=True)
    texto = models.CharField(max_length = 200, blank=True, unique=False)
    orden = models.IntegerField(blank=False)
    def __str__(self) -> str:
        return self.nombre