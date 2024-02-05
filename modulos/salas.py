from os import system
from .sistema import continuar, guardar, traejson
from . import sistema
import json
from .data import datos

def crear():
    cod= "S0"+str(len(datos["salas"]))
    datos={
        "cod_sala":cod,
        "nom_sala":input("ingrese el nombre de la sala: "),
        "capacida":int(input("Ingrese la capacidad de la sala: "))
    }
    datos["salas"][cod]=datos
    sistema.datos=datos
    guardar()

def msalas():
    datos=traejson()
    x=True
    while x:
        print("""
        \033[1;94mMenu Salas\033[0m
            1- Crear
            2- Editar
            3- Eliminar
            4- Listar
            5- Salir""")
        opc=int(input("\t"))
        system("clear")
        match(opc):
            case(1):
                crear()
            case(2):
                pass
            case(3):
                pass
            case(4):
                pass
            case(5):
                x=False
            case (_):
                print("otra vez")