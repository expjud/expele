from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
# por cada tabla una clase

class Expedien(models.Model):  
    texp = [('1','Exp'),('2','Inc'),('3','Otro')]     
    Tipexp = models.CharField(max_length=4,choices=texp,blank=True)
    Numeroexp = models.CharField(max_length=20, blank=True)
    Juzgadoexp = models.CharField(max_length=80, blank=True)
    Caratula = models.CharField(max_length=80,null=True)
    Resumen_caso = models.CharField(max_length=255,blank=True)
    Activo = models.BooleanField()
    Prioridad = models.BooleanField()
    #Fecha_aud = models.DateField(blank=True, null=True)
    Observacion = models.CharField(max_length=150,blank=True)       
    
    def __str__(self):
        return self.Caratula

class Audiencia(models.Model):  
    Audiencia_exp = models.ForeignKey(Expedien,on_delete=models.CASCADE,blank=True,null=True)
    Fecha = models.DateField(null=True)
    Juzgado = models.CharField(max_length=150,blank=True)
    Observacion = models.CharField(max_length=150,blank=True)
    def __str__(self):
        return self.Juzgado
    

class Pruebas(models.Model):  
    Pruebas_exp = models.ForeignKey(Expedien,on_delete=models.CASCADE,blank=True,null=True)
    Fecha = models.DateField(null=True)
    tipo_prueba = models.CharField(max_length=150,blank=True)
    Observacion = models.CharField(max_length=150,blank=True)
    def __str__(self):
        return self.tipo_prueba

class Tramite(models.Model):  
    Tramite_exp = models.ForeignKey(Expedien,on_delete=models.CASCADE,blank=True, null=True)
    Cabogado = models.BooleanField()
    Tasas = models.BooleanField()
    Derecho_archivo = models.BooleanField()
    Ser_parte = models.BooleanField()
    Dig_demanda = models.BooleanField()
    Crear_exp = models.BooleanField()
    Doc_24hs = models.BooleanField()
    Oficio_control = models.CharField(max_length=150,blank=True)
    Pridec_coptra = models.BooleanField()
    Pridec_cedpos = models.BooleanField()
    Observacion = models.CharField(max_length=150,blank=True)

    

class Pagos(models.Model): 
    Pagos_exp = models.ForeignKey(Expedien,on_delete=models.CASCADE,blank=True, null=True) 
    Fecha_pago = models.DateField(null=True)
    tpag = [('1','Honrario'),('2','Tasa'),('3','Gasto')]     
    Tip_pag = models.CharField(max_length=8,choices=tpag,blank=True)
    Monto_acordado =models.DecimalField(max_digits = 9,decimal_places=2)
    Pago_parcial =models.DecimalField(max_digits = 9,decimal_places=2)
    otro_pago = models.DecimalField(max_digits = 9,decimal_places=2)
    Observacion = models.CharField(max_length=150,blank=True)


   

class Cliente(models.Model):
    Cliente_exp = models.ForeignKey(Expedien,on_delete=models.CASCADE,blank=True, null=True)
    Nombre = models.CharField(max_length=80, blank=True)
    Num_documento = models.CharField(max_length=12, blank=True)
    Num_celular = models.CharField(max_length=12, blank=True)
    Correo = models.CharField(max_length=40, blank=True)
    Direccion = models.CharField(max_length=60, blank=True)
    Observacion = models.CharField(max_length=150,blank=True)

    def __str__(self):
        return self.Nombre

class Evento(models.Model):
    Evento_exp = models.ForeignKey(Expedien,on_delete=models.CASCADE,blank=True, null=True)
    Fecha_evento = models.DateField(null=True)
    Descripcion1 = models.CharField(max_length=150,null=True)
    Descripcion2 = models.CharField(max_length=150,null=True)
    Descripcion3 = models.CharField(max_length=150,null=True)

class Turno(models.Model):    
    Fecha_turno  = models.DateField(null=False)
    Hora_turno = models.CharField(max_length=10,blank=True)
    Nro_celular = models.CharField(max_length=11,blank=True)
    Nombre = models.CharField(max_length=80,blank=True)
    Tema = models.CharField(max_length=150,blank=True)
    Monto_consulta =models.DecimalField(max_digits = 9,decimal_places=2)
    Onservacion = models.CharField(max_length=150,blank=True)
    


class Documental(models.Model):
    Documental_exp = models.ForeignKey(Expedien,on_delete=models.CASCADE,blank=True, null=True)
    Fecha_doc = models.DateField(null=True)
    Cant_hojas = models.IntegerField()
    Descripcion1 = models.CharField(max_length=150,null=True)
    Descripcion2 = models.CharField(max_length=150,null=True)
    Descripcion3 = models.CharField(max_length=150,null=True)
    Guardada_en  = models.CharField(max_length=150,null=True)  






