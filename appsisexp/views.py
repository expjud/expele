from django.shortcuts import render, redirect
from appsisexp.models import Expedien, Pagos, Audiencia, Tramite, Pagos, Cliente, Evento, Documental,Pruebas
#from my_app import views
from django.db.models import Q
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
#from appreclamo.funciones import render_to_pdf
from django.http import HttpResponseRedirect, HttpResponse,FileResponse
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
#from django.http import Http404


# Create your views here.
@login_required(login_url='/')
def index(request):
    
    list_rec = Expedien.objects.all().order_by('-id')

    list_aud = Audiencia.objects.all().order_by('Fecha')   

    list_pru = Pruebas.objects.all().order_by('Fecha')   
            
    return render(request,"index.html", locals())

def expprio(request):
    
    list_rec = Expedien.objects.filter(Prioridad=True) 
                
    return render(request,"expprio.html", locals())

def priotodos(request):
    
    list_rec = Expedien.objects.all() 
                
    return render(request,"priotodos.html", locals())

def eventos(request):

    list_rec = Evento.objects.all().order_by('-Fecha_evento')     
    
    return render(request,"evento.html", locals())
    


    

# def laudiencia(request):
    
#     list_rec = Audiencia.objects.all() 
            
#     return render(request,"audiencia.html", locals())

def laudiencia(request,p):
    
    list_rec = Audiencia.objects.filter(Audiencia_exp_id=p)
    #list_rec = Audiencia.objects.all()
    #list_rec = Audiencia.objects.get(id=p)
            
    return render(request,"audiencia.html", locals())

def lprueba(request,p):
    
    list_rec = Pruebas.objects.filter(Pruebas_exp_id=p)
            
    return render(request,"pruebas.html", locals())



def ltramite(request,p):
    
    list_rec = Tramite.objects.filter(Tramite_exp_id=p)
    
    return render(request,"tramite.html", locals())
     
            
    

def lpagos(request,p):
    
    list_rec = Pagos.objects.filter(Pagos_exp_id=p)

    # nuevo
    #total = Pagos.objects.all().aggregate(total=Sum('Pago_parcial'))
    total = Pagos.objects.filter(Pagos_exp_id=p).aggregate(totalpar=Sum('Pago_parcial'))
    #total = Pagos.objects.filter(Pagos_exp_id=p).aggregate(sum('Pago_parcial'))
    #total = Pagos.objects.filter(Pagos_exp_id=p)
    #context = {'total':total}


    #
    return render(request,"pagos.html", locals())
    #return render(request,"pagos.html",context)

def lcliente(request,p):
    
    list_rec = Cliente.objects.filter(Cliente_exp_id=p)
    #list_rec = Audiencia.objects.all()
    #list_rec = Audiencia.objects.get(id=p)
            
    return render(request,"cliente.html", locals())

def levento(request,p):
    
    list_rec = Evento.objects.filter(Evento_exp_id=p)
            
    return render(request,"evento.html", locals())

def ldocument(request,p):
    
    list_rec = Documental.objects.filter(Documental_exp=p)
            
    return render(request,"documental.html", locals())

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)        
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request,f'Usuario {username} creado ')
            return redirect('index')
    else:
        form = UserRegisterForm()    

    context = {'form': form  }
    return render(request, "register.html", context)
