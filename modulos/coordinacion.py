from os import system
import json
from .sistema import continuar
from .data import datos
def guardar():
    with open("modulos/storage/data.json", "w") as f:
        data=json.dumps(datos, indent=4)
        f.write(data)
        f.close()
def modulos():
    lista=[]
    x=True
    while x:
        modulo={
            "cod_mod":int(input("Ingresa el codigo del modulo: ")),
            "nom_mod":str(input("Ingresa el nombre del modulo: ")),
            "temario":[str(input(f"ingrese el temario {i+1}: "))for i in range(int(input("Defina la cantidad de datos: ")))]
        }
        lista.append(modulo)
        x=continuar(x)
    return lista

def rutas():
    
    data={
        "cod_ruta":int(input("Ingrese el codigo de la ruta: ")),
        "nom_ruta":str(input("ingrese el nombre de la ruta: ")),
        "modulos":modulos()
    }
    datos["rutas"].append(data)
    guardar()
    return "Ruta Guardada"

def tabla():
    for i in datos["rutas"]:
        print(f"""
            ________________________________________
               -codigo- {i["cod_ruta"]}  -nombre- {i["nom_ruta"]}   
            ---------------Modulos------------------""")
        for b in i["modulos"]:
            print(f"""
              -{b["nom_mod"]}-
              nombre: {b["nom_mod"]}
              Temario: {"".join([f"{c} - " for c in b["temario"]])}
""")
def mcoordi():
    x=True
    while x:
        print("""
        Menu Camper
            1- Configurar Rutas
            2- 
            3- 
            4- 
            5- Salir""")
        opc=int(input("\t"))
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
                system("clear")
                x=False
            case (_):
                print("otra vez")
def menurutas():
    y=True
    while y:
        print("""
        Menu Camper
            1- Crear ruta
            2- Editar rutas
            3- Asignar rutas
            4- Eliminar Camper
            5- Salir""")
        opc=int(input("\t"))
        match(opc):
            case(1):
                rutas()
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