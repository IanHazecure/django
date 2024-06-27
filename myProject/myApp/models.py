from django.db import models

# Create your models here.

class Productos(models.Model):
    id_produ        = models.AutoField(db_column = 'idProdu', primary_key=True)
    nombre_producto = models.CharField(max_length=50)
    id_tipo         = models.ForeignKey('TipoProducto', models.DO_NOTHING, db_column='idTipo', null=True)
    precio          = models.IntegerField()
    foto            = models.ImageField(upload_to='media', null=True)
    stock           = models.IntegerField(null = True) 

class TipoProducto(models.Model):
    id_tipo         = models.AutoField(db_column = 'idTipo', primary_key=True)
    nombre_tipo     = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_tipo 