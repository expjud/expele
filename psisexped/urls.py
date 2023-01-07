"""psisexped URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#from django.contrib.auth import views as auth_views
from django.urls import path, re_path
#from django.views import View
from appsisexp import views
from django.conf import settings
#from django.views.static import serve
from django.conf.urls.static import static
from django.conf.urls import url 
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('index/admin/', admin.site.urls),
    
    #path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    
    path('index/expprio/', views.expprio, name='expprio'),

    path('index/evento/', views.eventos, name='evento'),
    
   
    



    #path('lisaudi/', views.laudiencia, name='audi'),
    #re_path(r'^lisaudi/$', views.laudiencia, name='lisaudi'),  
    #path('reclam/generarReclamoPDF/<int:p>',views.GenerarReclamoPDF, name='generarReclamoPDF'),   
    path('index/lisaudi/<int:p>', views.laudiencia, name='lisaudi'),
    path('index/lprueba/<int:p>', views.lprueba, name='lprueba'),
    path('index/listram/<int:p>', views.ltramite, name='listram'),    
    path('index/lispag/<int:p>', views.lpagos, name='lispag'),
    path('index/liscli/<int:p>', views.lcliente, name='liscli'),    
    path('index/levento/<int:p>', views.levento, name='levento'),    
    path('index/ldocument/<int:p>', views.ldocument, name='ldocument'), 
    path('register/', views.register, name='register'),  
    #path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),        
    

# ]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)