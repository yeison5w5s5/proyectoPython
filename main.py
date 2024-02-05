from os import system
from modulos import sistema, camper, trainer, coordinacion, data, ruta
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
def actualizar(x):
    if x==1:
         camper.datos=sistema.traejson()
Ban=True
while Ban:
    system("clear")
    menu()
    opc=int(input("\t"))
    match(opc):
        case(1):
            camper.datos=sistema.traejson()
            camper.mcamper()
        case(2):
            trainer.datos=sistema.traejson()
            trainer.mtrainer()
        case(3):
            coordinacion.datos=sistema.traejson()
            coordinacion.mcoordi()
        case(4):
            system("clear")
            print("\t===Fin===")
            Ban=False
        case(_):
            print("otra vez")