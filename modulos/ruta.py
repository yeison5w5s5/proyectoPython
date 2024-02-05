from os import system
import json
import readline
from . import sistema
from .sistema import continuar, guardar, traejson
from .data import datos

def tbMod(i):    
    for b in i["modulos"]:
        print(f"""
            -{b}-{i["modulos"][b]["nom_mod"]}-
            nombre: {i["modulos"][b]["nom_mod"]}
            Temario: {"".join([f"{c} - " for c in i["modulos"][b]["temario"]])}""")

def tbRuta(i):
    ruta=datos["rutas"][i]
    print(f"""
            ________________________________________
               -codigo- {i}  -nombre- {ruta["nom_ruta"]}   
            ---------------Modulos------------------""")
    tbMod(ruta)

def tbRutas():
    for i in datos["rutas"]:
        tbRuta(i)

def modulos(codigo):
    lista=datos["rutas"][str(codigo)]["modulos"] if codigo!="" else {}
    print(lista)
    x=True
    while x:
        codigo=input("Ingresa el codigo del modulo: ")
        if codigo in lista:
            print("\033[1;33mYa hay un modulo con este codigo\033[0m")
        else:
            modulo={
                "cod_mod":codigo,
                "nom_mod":str(input("Ingresa el nombre del modulo: ")),
                "temario":[str(input(f"ingrese el temario {i+1}: "))for i in range(int(input("Defina la cantidad de datos: ")))]
            }
            lista[str(codigo)]=modulo
        x=continuar()
    return lista

def rutas(codigo):
    data={
        "cod_ruta":codigo,
        "nom_ruta":str(input("ingrese el nombre de la ruta: ")),
        "modulos":modulos("")
    }
    datos["rutas"][str(codigo)]=data
    sistema.datos=datos
    guardar()
    return "Ruta Guardada"

def editRuta():
    datos=traejson()
    while True:
        tbRutas()
        codigo=input("Ingresa el codigo de la ruta a editar: ")
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
                    modulos(codigo)
                    guardar()
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
        guardar()
        system("clear")
        print("\033[1;31m\tEliminado\033[0m")
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
                def prueba():
                    codigo=input("ingrese el codigo de la ruta:")
                    if codigo in datos["rutas"]:
                        print("\033[1;33mYa hay una ruta con este codigo\033[0m")
                        return "bye" if continuar()==False else prueba()
                    else:
                        rutas(codigo)
                prueba()
            case(2):
                editRuta()
            case(3):
                eliminarR()
            case(4):
                system("clear")
                y=False
            case (_):
                print("otra vez")


    
