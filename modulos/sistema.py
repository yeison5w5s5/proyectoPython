from os import system
import json
from .data import datos
def continuar():
    X=True
    print("""
        ¿Quieres continuar?
               1=Si
               2=No""")
    opc=int(input(""))
    while True:
        match(opc):
            case(1):
                x=True
                break
            case(2):
                x=False
                break
            case(_):
                print("opcion no disponible")
    return x

def guardar():
    with open("modulos/storage/data.json", "w") as f:
        data=json.dumps(datos, indent=4)
        f.write(data)
        f.close()
    print("\t\033[1;32mguardado\033[0m")
def traejson():
    system("clear")
    with open("modulos/storage/data.json", "r") as f:
                datos=json.loads(f.read())
                f.close()
                return datos
