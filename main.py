from os import system
from modulos import camper, trainer, coordinacion
import json

def menu():
    print("""
    Este es el menu principal
        1- Menu Camper
        2- Menu Trainer
        3- Menu Coordinacion
        4- Salir""")
def traejson():
    system("clear")
    with open("modulos/storage/data.json", "r") as f:
                datos=json.loads(f.read())
                f.close()
                return datos
Ban=True
while Ban:
    system("clear")
    menu()
    opc=int(input("\t"))
    match(opc):
        case(1):
            pass
        case(2):
            pass
        case(3):
            camper.rutas=traejson()
            coordinacion.coordi()
        case(4):
            system("clear")
            print("\t===Fin===")
            Ban=False
        case(_):
            print("otra vez")