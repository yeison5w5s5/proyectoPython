from os import system
import json
import readline
from . import sistema
from .sistema import continuar, guardar, traejson, preingreso, enteros
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
    if codigo=="":
        codigo=str.upper(input("ingrese el codigo de la ruta: "))
    if codigo not in datos["rutas"]:
        editRuta(codigo) if continuar(1)==False else asigMod(codigo)
    else:
        if datos["rutas"][codigo]["modulos"]!=[]:
            print("\t-------Sus modulos---------")
        tbMod(datos["rutas"][codigo])
        print("\t-------para agregar---------")
        for i in dict(list(datos["modulos"].items())[1:]):
            if i not in datos["rutas"][codigo]["modulos"]:
                tbMod1(i)
        while True:
            cod=str.upper(input("ingrese el codigo del modulo que quiere agregar: "))
            if cod in datos["modulos"]:
                if cod not in datos["rutas"][codigo]["modulos"]:
                    datos["rutas"][codigo]["modulos"].append(cod)
                else:
                    print ("Ya tienes este modulo")
            else:
                if continuar(1)==False:
                    break
            if continuar("")==False:
                sistema.datos=datos
                guardar(1)
                editRuta(codigo)

def delModR(codigo):
    if datos["rutas"][codigo]["modulos"]!=[]:
            print("\t-------Sus modulos---------")
    tbMod(datos["rutas"][codigo])
    while True:
        cod=str.upper(input("ingrese el codigo del modulo que quiere eliminar: "))
        if cod in datos["rutas"][codigo]["modulos"]:
            datos["rutas"][codigo]["modulos"].remove(cod)
        else:
            if continuar(1)==False:
                break
        if continuar("")==False:
            sistema.datos=datos
            guardar(2)
            editRuta(codigo)
def modulos():
    x=True
    while x:
        cod="M0"+str(datos["modulos"]["cont"])
        modulo={
            "cod_mod":cod,
            "nom_mod":str(input("Ingresa el nombre del modulo: ")),
            "temario":[str(input(f"ingrese el temario {i+1}: "))for i in range(enteros("Defina la cantidad de datos: "))]
        }
        datos["modulos"][cod]=modulo
        datos["modulos"]["cont"]+=1
        if continuar("")==False:
            sistema.datos=datos
            guardar(1)
            menurutas()
            

def rutas(cod):
    codigo,nom= ["R0"+str(datos["rutas"]["cont"])," "] if cod=="" else [cod,datos["rutas"][cod]["nom_ruta"]]
    data={
        "cod_ruta":codigo,
        "nom_ruta":preingreso("ingrese el nombre de la ruta: ",nom),
        "modulos":[]
    }
    datos["rutas"][codigo]=data
    datos["rutas"]["cont"]+=1
    sistema.datos=datos
    guardar(1)
    menurutas() if cod=="" else editRuta()

def editRuta(cc):
    datos=traejson()
    while True:
        if cc=="":
            tbRutas()
            codigo=str.upper(input("Ingresa el codigo de la ruta a editar: "))
            if codigo in datos["rutas"]:
                system("clear")
                tbRuta(codigo)
            else:
                if continuar(1)==False:
                    menurutas()
        else:
            codigo=cc
            tbRuta(codigo)
        print("""
            \033[1;94mMenu de edicion de ruta\033[0m
            1- Editar Ruta
            2- Agregar modulos
            3- Eliminar modulos
            4- Salir""")
        opc=input()
        match(opc):
            case("1"):
                rutas(codigo)
            case("2"):
                asigMod(codigo)
            case("3"):
                delModR(codigo)
            case("4"):
                menurutas()
            case (_):
                print("opcion no identificada")
def eliminarR():
    tbRutas()
    cc=str.upper(input("ingresa el cod de la ruta que quieres eliminar: "))
    if cc in datos["rutas"]:
        tbRuta(cc)
        print("¿Esta es la ruta que quieres eliminar?")
        datos["rutas"].pop(cc) if continuar("")==True else menurutas()
        sistema.datos=datos
        guardar(2)
    else:
        return eliminarR() if continuar(1)==True else menurutas()
def menurutas():
    y=True
    while y:
        print("""
        \033[1;94mMenu Rutas\033[0m
            1- Crear ruta
            2- Editar rutas
            3- Crear modulos
            4- Eliminar ruta
            0- Salir""")
        opc=input("\t")
        system("clear")
        match(opc):
            case("1"):
                rutas("")
            case("2"):
                editRuta("")
            case("3"):
                modulos()
            case("4"):
                eliminarR()
            case("0"):
                system("python3 main.py")
            case (_):
                print("otra vez")


    
