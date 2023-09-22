from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import  HttpResponse

# Create your views here.

def home(request):
    return render(request, "home.html")

def signup(request):
    if request.method == "GET":
        return render(request, "signup.html", {
        "form": UserCreationForm
    })
    else:
        #Si el pass1 es igual al pass2 podemos avanzar para crear un usuario nuevo
        if request.POST["password1"] == request.POST["password2"]:
            #Intentamos registrar el usuario en la base de datos
            try:
                #Obtenemos los datos y los guardamos en un variable 
                user =    User.objects.create_user(username= request.POST["username"], password = request.POST["password1"])
                #Guardamos los datos en la base de datos
                user.save()
                return render(request, "signup.html", {
                    "form": UserCreationForm,
                    "error": "Usuario Creado"
                })
            except:
                #Si falla salta un alert
                return render(request, "signup.html", {
                    "form": UserCreationForm,
                    "error": "Usuario Existente"
                })
                
            
        return render(request, "signup.html",{
            "form": UserCreationForm,
            "error": "Contraseñas no coinciden"
        })
        
    

