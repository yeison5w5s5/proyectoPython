from os import system
import json
import readline
from .sistema import continuar, traejson
from .data import datos
from .ruta import menurutas
from .salas import msalas
from . import salas, ruta 


def preingreso(mensaje, valor_predeterminado):
    readline.set_startup_hook(lambda: readline.insert_text(valor_predeterminado))
    try:
        entrada_usuario = input(f'{mensaje}')
    finally:
        readline.set_startup_hook()
    return entrada_usuario



def listar(x):
        for i in datos[x]:
            for v in datos[x][i]:
                print("{:<15}".format(v),end="")
            print("\n")
            break
        for i in datos[x]:
            for v in datos[x][i]:
                print("{:<15}".format(str(datos[x][i][v]),),end="")
            print("\n")

# def asignar():
#     cc="AS"+str(len(datos["asig"]))
#     listar("camper")
#     cCamper=input("dijita la identificacion del camper: ")
#     if cCamper in datos["camper"]:
#         listar("trainer")
#         cTrainer=input("dijita la identificacion del Trainer: ")
#         if cTrainer in datos["trainer"]:

#     info={

#     }

def masignacion():
    y=True
    while y:
        print("""
        \033[1;94mMenu Asignacion\033[0m
            1- Crear asignacion
            2- Editar asignacion
            3- Eliminar asignacion
            4- Salir""")
        opc=int(input("\t"))
        system("clear")
        match(opc):
            case(1):
                asignar()
            case(2):
                editRuta()
            case(3):
                pass
            case(4):
                system("clear")
                y=False
            case (_):
                print("otra vez")

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
        opc=int(input("\t"))
        system("clear")
        match(opc):
            case(1):
                ruta.datos=traejson()
                menurutas()
            case(2):
                pass
            case(3):
                pass
            case(4):
                pass
            case(5):
                salas.datos=traejson()
                msalas()
            case(6):
                x=False
            case (_):
                print("otra vez")


