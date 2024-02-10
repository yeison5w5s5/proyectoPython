from os import system
import json
from .sistema import continuar, traejson
from .data import datos
from . import salas, ruta ,asignacion

def mcoordi():
    x=True
    while x:
        print("""
        \033[1;94mMenu Coordinacion\033[0m
            1- Rutas
            2- Asignaciones
            3- Trainer
            4- Camper
            5- Salas
            6- Salir""")
        opc=input("\t")
        system("clear")
        match(opc):
            case "1":
                ruta.datos=traejson()
                ruta.menurutas()
            case "2":
                asignacion.datos=traejson()
                asignacion.masignacion()
            case "3":
                pass
            case "4":
                pass
            case "5":
                salas.datos=traejson()
                salas.msalas()
            case "6":
                x=False
            case (_):
                print("otra vez")


