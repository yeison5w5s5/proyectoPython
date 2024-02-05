from os import system
import json
import readline
from .sistema import continuar
from .data import datos
from .ruta import menurutas, datos
from . import ruta

def traejson():
    system("clear")
    with open("modulos/storage/data.json", "r") as f:
                datos=json.loads(f.read())
                f.close()
                return datos
def guardar():
    with open("modulos/storage/data.json", "w") as f:
        data=json.dumps(datos, indent=4)
        f.write(data)
        f.close()
    datos=traejson()

def preingreso(mensaje, valor_predeterminado):
    readline.set_startup_hook(lambda: readline.insert_text(valor_predeterminado))
    try:
        entrada_usuario = input(f'{mensaje}')
    finally:
        readline.set_startup_hook()
    return entrada_usuario




def mcoordi():
    ruta.datos=traejson()
    x=True
    while x:
        print("""
        \033[1;94mMenu Coordinacion\033[0m
            1- Rutas
            2- 
            3- 
            4- 
            5- Salir""")
        opc=int(input("\t"))
        system("clear")
        match(opc):
            case(1):
                menurutas()
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


