from os import system
from modulos import camper, trainer, coordinacion, data, ruta
import json

def menu():
    print()
    print(f"""
    \033[1;94m Este es el menu principal 
        ¿Cual es tu rol?\033[0m
           1- Camper
           2- Trainer
           3- Coordinacion
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
            camper.datos=traejson()
            camper.mcamper()
        case(2):
            pass
        case(3):
            coordinacion.datos=traejson()
            coordinacion.mcoordi()
        case(4):
            system("clear")
            print("\t===Fin===")
            Ban=False
        case(_):
            print("otra vez")