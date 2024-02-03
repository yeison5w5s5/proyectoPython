from os import system
import json
import readline
from .sistema import continuar
from .data import datos

def guardar():
    with open("modulos/storage/data.json", "w") as f:
        data=json.dumps(datos, indent=4)
        f.write(data)
        f.close()

def preingreso(mensaje, valor_predeterminado):
    readline.set_startup_hook(lambda: readline.insert_text(valor_predeterminado))
    try:
        entrada_usuario = input(f'{mensaje}')
    finally:
        readline.set_startup_hook()
    return entrada_usuario

def tbMod(i):    
    for b in i["modulos"]:
        print(f"""
            -{b["cod_mod"]}-{b["nom_mod"]}-
            nombre: {b["nom_mod"]}
            Temario: {"".join([f"{c} - " for c in b["temario"]])}""")
def tbRuta(i):
    print(f"""
            ________________________________________
               -codigo- {i["cod_ruta"]}  -nombre- {i["nom_ruta"]}   
            ---------------Modulos------------------""")
    tbMod(i)
def tbRutas():
    for i in datos["rutas"]:
        tbRuta(i)
        


def mcoordi():
    x=True
    while x:
        print("""
        \033[1;94mMenu Coordinacion\033[0m
            1- Configurar Rutas
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


def modulos():
    x=True
    lista=[]
    while x:
        modulo={
            "cod_mod":int(input("Ingresa el codigo del modulo: ")),
            "nom_mod":str(input("Ingresa el nombre del modulo: ")),
            "temario":[str(input(f"ingrese el temario {i+1}: "))for i in range(int(input("Defina la cantidad de datos: ")))]
        }
        lista.append(modulo)
        x=continuar(x)
    return lista

def rutas(cod_ruta):
    idxx=0
    if cod_ruta=="":
        a=b=c=""
    else:
        for idx,i in enumerate(datos["rutas"]):
            if int(i["cod_ruta"])==int(cod_ruta):
                idxx=idx
                a=cod_ruta
                b=i["nom_ruta"]
                c=i["modulos"]
        
    data={
        "cod_ruta":int(preingreso("Ingrese el codigo de la ruta: ", a)),
        "nom_ruta":str(preingreso("ingrese el nombre de la ruta: ", b)),
        "modulos":modulos() if cod_ruta=="" else c
    }
    if cod_ruta=="":
        datos["rutas"].append(data)
    else:
        datos["rutas"][idxx]["cod_ruta"]=data["cod_ruta"]
        datos["rutas"][idxx]["nom_ruta"]=data["nom_ruta"]
    guardar()
    return "Ruta Guardada"

def editRuta():
    while True:
        tbRutas()
        codigo=input("Ingresa el codigo de la ruta a editar: ")
        [tbRuta(i) for i in datos["rutas"] if int(i["cod_ruta"])==int(codigo)]
        if continuar==False:
            break
        print("""
            \033[1;94mMenu de edicion de ruta\033[0m
            1- Editar Ruta
            2- Agregar modulos
            3- Rehacer ruta""")
        opc=int(input())
        match(opc):
            case(1):
                rutas(codigo)


def menurutas():
    y=True
    while y:
        print("""
        \033[1;94mMenu Rutas\033[0m
            1- Crear ruta
            2- Editar rutas
            3- Asignar rutas
            4- Eliminar Camper
            5- Salir""")
        opc=int(input("\t"))
        system("clear")
        match(opc):
            case(1):
                rutas("")
            case(2):
                editRuta()
            case(3):
                pass
            case(4):
                pass
            case(5):
                system("clear")
                y=False
            case (_):
                print("otra vez")