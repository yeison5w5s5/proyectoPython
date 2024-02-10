from os import system
from .data import datos
from .sistema import continuar, guardar
from . import sistema, asignacion
import json

def login():
    grupos=[]
    cTrainer= input("ingresa tu numero de identificacion: ")
    if cTrainer not in datos["trainer"]:
        login() if continuar(2)==True else mtrainer()
    else:
        for i in datos["asig"]:
            if datos["asig"][i]["cc_trainer"]==cTrainer:
                asignacion.datos=datos
                print(asignacion.printgrupo(i))
                grupos.append(i)
        if grupos==[]:
            print("aun no tienes grupos asignados")
        else:
            cGrupo= str.upper(input("ingresa el codigo del grupo que quieres ver: "))
            if cGrupo not in grupos:
                print("codigo no identificado")

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
            "cod_horario":[input(f'\n{i}- {datos["horarios"][i]}: ') for i in datos["horarios"]],
            "Estado":"pendiente"
        }
        datos["trainer"][cc]=data
        sistema.datos=datos
        guardar(1)
    return data

def mtrainer():
    y=True
    while y:
        print("""
        \033[1;94mMenu Trainer\033[0m
            1- Registro
            2- Ingreso
            3- 
            4- Eliminar Camper
            5- Salir""")
        opc=input("\t")
        system("clear")
        match(opc):
            case("1"):
                info()
            case("2"):
                login()
            case("3"):
                pass
            case("4"):
                pass
            case("5"):
                system("clear")
                y=False
            case (_):
                print("otra vez")