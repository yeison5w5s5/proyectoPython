from os import system
import json
from .sistema import continuar, traejson
from .data import datos
from . import salas, ruta ,asignacion, informes, trainer

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
            6- informes
            0- Salir""")
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
                trainer.datos=traejson()
                trainer.estadoTrai()
            case "5":
                salas.datos=traejson()
                salas.msalas()
            case "6":
                informes.datos=traejson()
                informes.minformes()
            case "0":
                system("python3 main.py")
            case (_):
                print("otra vez")


