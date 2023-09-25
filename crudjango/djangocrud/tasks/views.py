from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import  HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

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
                    #Obtenemos los datos y los guardamos en un variable user 
                    user =    User.objects.create_user(username= request.POST["username"], password = request.POST["password1"])
                    #Guardamos los datos en la base de datos
                    user.save()
                    #Creamos una cookies
                    login(request, user)
                    #Redireccionamos al view tasks
                    return redirect("tasks")
                
                #Si ya existe un usuario, marca error
                except:
                    return render(request, "signup.html", { #Volvemos a retornar el formulario
                        "form": UserCreationForm, #Imp formulario base de django
                        "error": "User ya existe" #Mensaje de error
                    })

        #Si contraseña1 y contraseña2 no coinciden marca error y redirecciona nuevamente a signup
        return render(request, "signup.html",{ #Volvemos a retornar el registro (signup.html)
            "form": UserCreationForm, #Formulario base de django
            "error": "Contraseñas no coinciden" #Mensaje de error
        })

#funcion de tasks
def tasks(request):
    return render(request, "tasks.html") #Retornamos tasks.html

#Logout
def signout(request):
    logout(request)
    #Redireccionamos a home cuando el usuario salga
    return redirect("home")

#Sign in, login
def signin(request):
    
    #Sino me esta enviando datos, mostramos esto
    if request.method == "GET":
        return render(request, "signin.html", {
            "form": AuthenticationForm
        })
        
    else:
        
        #creamos user, donde se almacea todos los datos del login
        user = authenticate(
            request, username = request.POST["username"], password  = request.POST["password"])
        
        if user in None: #Si no se consigue el usuario mostrara lo siguiente
            
            return render(request, "signin.html", { #Retornamos
                "form": AuthenticationForm, #formulario
                "error": "Usuario o contraseña invalidos" #Mensaje de error
            })
            
        else:
            
            login(request, user) #Guardamos el usuario
            
            return redirect("tasks") #Redireccionamos a tasks(pagina)

