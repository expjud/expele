from django.contrib import admin
from django.contrib.auth.models import Group

from appsisexp.models import Expedien, Audiencia, Tramite, Pagos, Cliente,Evento,Documental,Pruebas,Turno 
     

# Register your models here.

# nuevo
# class ExpedTabularInline(admin.TabularInline):
#     model = Expedien


#


class ExpedAdmin(admin.ModelAdmin):
#
    model = Expedien
#    
    list_display=("Tipexp","Numeroexp","Caratula", "Resumen_caso", "Observacion")
       
    list_filter=("Prioridad","Activo",)

    #agrago un buscador
    #search_fields=("Numeroexp", "Caratula")
    search_fields=("Caratula",)

    

# nuevo ojo     
class audienciaAdmin(admin.ModelAdmin):
    model = Audiencia

    list_display=("Audiencia_exp","Fecha","Juzgado","Observacion")

# nuevoooo
    autocomplete_fields = ['Audiencia_exp',]
    # ------


class TurnoAdmin(admin.ModelAdmin):
    model = Turno

    list_display=("Fecha_turno","Hora_turno","Nro_celular","Nombre","Tema","Monto_consulta","Onservacion")

class pruebasAdmin(admin.ModelAdmin):
    
    model = Pruebas

    list_display=("Pruebas_exp","Fecha","tipo_prueba","Observacion")

    autocomplete_fields = ['Pruebas_exp',]



    
   
# nuevo    
class PagosAdmin(admin.ModelAdmin):
    model = Pagos

    list_display=("Pagos_exp","Fecha_pago","Tip_pag","Monto_acordado","Pago_parcial")

    # nuevoooo
    autocomplete_fields = ['Pagos_exp',]
    # ------

class TramiteAdmin(admin.ModelAdmin):
    model = Tramite

    list_display=("Tramite_exp","Cabogado","Tasas","Derecho_archivo","Ser_parte","Dig_demanda","Crear_exp","Doc_24hs","Oficio_control","Pridec_coptra","Pridec_cedpos","Observacion")

    # nuevoooo
    autocomplete_fields = ['Tramite_exp',]
    # ------
    
class EventoAdmin(admin.ModelAdmin):
    model = Evento

    list_display=("Fecha_evento","Evento_exp","Descripcion1","Descripcion2","Descripcion3")
    # nuevoooo
    autocomplete_fields = ['Evento_exp',]
    # ------

class DocumentAdmin(admin.ModelAdmin):
    model = Documental

    list_display=("Documental_exp","Fecha_doc","Cant_hojas","Guardada_en")
     # nuevoooo
    autocomplete_fields = ['Documental_exp',]
    # ------


class ClienteAdmin(admin.ModelAdmin):
    model = Cliente

    list_display=("Cliente_exp",'Nombre','Num_celular','Observacion')
     # nuevoooo
    autocomplete_fields = ['Cliente_exp',]
    # ------


# nuevo
# class AudiAdmin(admin.ModelAdmin):
#     inlines = [ExpedTabularInline]
#     model = Audiencia
    
#     list_display=("Fecha", "Juzgado","Observacion")
# nuevo


admin.site.register(Expedien,ExpedAdmin)

admin.site.register(Audiencia,audienciaAdmin)

admin.site.register(Pruebas,pruebasAdmin)
admin.site.register(Turno,TurnoAdmin)

admin.site.register(Tramite,TramiteAdmin)
admin.site.register(Pagos,PagosAdmin)
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Evento,EventoAdmin)
admin.site.register(Documental,DocumentAdmin)


# fin nuevo
admin.site.site_header = "SISTEMA DE EXPEDIENTES" 