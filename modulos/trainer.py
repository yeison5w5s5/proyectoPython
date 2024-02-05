from os import system
from .data import datos
from .sistema import continuar, guardar
from . import sistema
import json

def info():
    cc=input("ingresa tu numero de  ID: ")
    if str(cc) in datos["trainer"]:
        print("Este numero ya existe")
        info()
    else:
        nombre=str.upper(input("Ingrese su nombre: "))
        print("""
            Para elegir el horario dijita 
                1=disponible
                0=no disponible
            Frente a cada horario""")
        data={
            "cc_trainer":cc,
            "nom_trainer":nombre,
            "cod_horaio":[input(f'\n{i}- {datos["horarios"][i]}: ') for i in datos["horarios"]],
        }
        datos["trainer"][cc]=data
        sistema.datos=datos
        guardar()
    return data

def mtrainer():
    y=True
    while y:
        print("""
        \033[1;94mMenu Trainer\033[0m
            1- Registro
            2- 
            3- 
            4- Eliminar Camper
            5- Salir""")
        opc=int(input("\t"))
        system("clear")
        match(opc):
            case(1):
                info()
            case(2):
                pass
            case(3):
                pass
            case(4):
                pass
            case(5):
                system("clear")
                y=False
            case (_):
                print("otra vez")