from os import system
import json
from sistema import continuar
from data import rutas
def modulos():
    lista=[]
    x=True
    while x:
        modulo={
            "cod_mod":int(input("Ingresa el codigo del modulo: ")),
            "nom_mod":str(input("Ingresa el nombre del modulo: ")),
            "temario":str(input("ingresa el temario del modulo: "))
        }
        lista.append(modulo)
        x=continuar(x)
    return lista

def rutas():
    data={
        "cod_ruta":int(),
        "nom_ruta":str(input("ingrese el nombre de la ruta: ")),
        "modulos":modulos()
    }
    return data

def mcoordi():
    Ban=True
    while Ban:
        print("""
        Menu Camper
            1- Guardar ruta
            2- Buscar Camper
            3- Editar Camper
            4- Eliminar Camper
            5- Salir""")
        opc=int(input("\t"))
        match(opc):
            case(1):
                datos["rutas"].append(rutas())
                print(datos)
            case(2):
                pass
            case(3):
                pass
            case(4):
                pass
            case(5):
                system("clear")
                Ban=False
            case (_):
                print("otra vez")
