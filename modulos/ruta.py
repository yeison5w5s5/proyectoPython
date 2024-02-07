from os import system
import json
import readline
from . import sistema
from .sistema import continuar, guardar, traejson
from .data import datos

def tbMod1(b):
    print(f"""
            -{b}-{datos["modulos"][b]["nom_mod"]}-
            Temario: {"".join([f"{c} - " for c in datos["modulos"][b]["temario"]])}""")

def tbMod(i):    
    for b in i["modulos"]:
        tbMod1(b)

def tbRuta(i):
    ruta=datos["rutas"][i]
    print(f"""
            ________________________________________
               -codigo- {i}  -nombre- {ruta["nom_ruta"]}   
            ---------------Modulos------------------""")
    tbMod(ruta)

def tbRutas():
    for i in dict(list(datos["rutas"].items())[1:]):
        tbRuta(i)
def asigMod(codigo):
    codigo=str.upper(input("ingrese el codigo de la ruta: "))
    if codigo in datos["rutas"]:
        print("\t-------Sus modulos---------")
        tbMod(datos["rutas"][codigo])
        print("\t-------para agregar---------")
        for i in datos["modulos"]:
            if i not in datos["rutas"][codigo]["modulos"]:
                tbMod1(i)
        

    
    lista=datos["rutas"][str(codigo)]["modulos"] if codigo!="" else []

def modulos():
    x=True
    while x:
        cod="M0"+str(datos["rutas"]["cont"][1])
        modulo={
            "cod_mod":cod,
            "nom_mod":str(input("Ingresa el nombre del modulo: ")),
            "temario":[str(input(f"ingrese el temario {i+1}: "))for i in range(int(input("Defina la cantidad de datos: ")))]
        }
        datos["modulos"][cod]=modulo
        datos["modulos"]["cont"]+=1
        if continuar()==False:
            sistema.datos=datos
            guardar(1)
            menurutas()
            
    return lista

def rutas():
    codigo="R0"+str(datos["rutas"]["cont"][0])
    data={
        "cod_ruta":codigo,
        "nom_ruta":str(input("ingrese el nombre de la ruta: ")),
        "modulos":modulos("")
    }
    datos["rutas"][str(codigo)]=data
    datos["rutas"]["cont"][0]+=1
    sistema.datos=datos
    guardar(1)
    return "Ruta Guardada"

def editRuta():
    datos=traejson()
    while True:
        tbRutas()
        codigo=str.upper(input("Ingresa el codigo de la ruta a editar: "))
        if codigo in datos["rutas"]:
            tbRuta(codigo)
            if continuar==False:
                break
            print("""
                \033[1;94mMenu de edicion de ruta\033[0m
                1- Editar Ruta
                2- Agregar modulos
                3- Salir""")
            opc=int(input())
            match(opc):
                case(1):
                    rutas(codigo)
                case(2):
                    asigMod(codigo)
                case(3):
                    menurutas()
                case (_):
                    print("opcion no identificada")

        else:
            print("No se encontro ruta con este codigo")
            if continuar()==False:
                break

def eliminarR():
    tbRutas()
    cc=input("ingresa el cod de l aruta que quieres eliminar: ")
    if cc in datos["rutas"]:
        tbRuta(cc)
        print("¿Esta es la ruta que quieres eliminar?")
        datos["rutas"].pop(cc) if continuar()==True else menurutas()
        sistema.datos=datos
        guardar(2)
    else:
        print("Codigo no identificado:")
        return eliminarR() if continuar()==True else "bye"
def menurutas():
    y=True
    while y:
        print("""
        \033[1;94mMenu Rutas\033[0m
            1- Crear ruta
            2- Editar rutas
            3- Eliminar ruta
            4- Salir""")
        opc=int(input("\t"))
        system("clear")
        match(opc):
            case(1):
                rutas()
            case(2):
                editRuta()
            case(3):
                eliminarR()
            case(4):
                system("clear")
                y=False
            case (_):
                print("otra vez")


    
