from django.shortcuts import render
from django.http import HttpResponse


class Pilotos:
    numero = ""
    nombre = ""
    nacionalidad = ""
    equipo = ""

    def __init__(self, numero, nombre, nacionalidad, equipo):
        self.numero = numero
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.equipo = equipo
        
    
    def getNumero(self):
        return self.numero
    
    def getNombre(self):
        return self.nombre
    
    def getNacionalidad(self):
        return self.nacionalidad

    def getEquipo(self):
        return self.equipo

objPilto1 = Pilotos("44","Lewis Hamilton","Británico","Mercedes AMG Petronas F1 Team")
objPilto2 = Pilotos("1","Max Verstappen","Neerlandesa","Red Bull Racing ")
objPilto3 = Pilotos("16","Charles Leclerc","Mónaco","Scuderia Ferrari")
objPilto4 = Pilotos("4","Lando Norris","Británico","McLaren Racing ")



def home(request):
    return render(request, "home.html", {
        "piloto1":objPilto1,
        "piloto2":objPilto2,
        "piloto3":objPilto3,
        "piloto4":objPilto4
    })
    
    