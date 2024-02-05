from os import system
import json
from .data import datos
from .sistema import continuar, guardar, traejson
from . import sistema

def info(cc):
    data={
        "cc_camper":cc,
        "nom_camper":str.upper(input("Ingrese su nombre: ")),
        "apell_camper":str.upper(input("Ingrese su apellido: ")),
        "edad_camper":int(input("Ingrese su edad: ")),
        "Dirr_camper":str.upper(input("Ingrese su direccion: ")),
        "Estado":"preinscrito",
        "cc_acudi":input("Ingrse numnero de identifiacion del acudiente: "),
        "nom_acudiente":str.upper(input("Ingrse nombre completo de su acudiente: ")),
    }
    return data

def guardarcam():
    cc=input("Ingrese numero de identificacion: ")
    if str(cc) in datos["camper"]:
        print("Este numero ya existe")
        guardarcam()
    else:
        datos["camper"][cc]=info(cc)
        sistema.datos=datos
        guardar()
    return "Camper"    
def buscar():
    datos=traejson()
    system("clear")
    codigo=input("Ingresa tu numero de identificacion: ")
    if codigo in datos["camper"]:
        camper=datos["camper"][codigo]
        print(f"""
                \033[1;94mTus Datos\033[0m
            ----------------------------
            Identificacion: {camper["cc_camper"]}
            Nombre: {camper["nom_camper"]}
            Apellido: {camper["apell_camper"]}
            Edad: {camper["edad_camper"]}
            Direccion: {camper["Dirr_camper"]}
            CC_acudiente: {camper["cc_acudi"]}
            Nombre: {camper["nom_acudiente"]}
            Estado: {camper["Estado"]}""")
    else:
        print("Numero de identificacion no reconocido")
        if continuar()==True:
            buscar() 

'''def editar():
    system("clear")
    print("""
                ___________________________
                * Acualizacion del camper *
                ___________________________
    """)
    codigo = int(input("Ingrese el codigo del camper que deseas actualizar: "))
    camper1(codigo)
    print("¿Este es el camper que deseas actualizar?")
    bandera=True
    while (bandera):
        print("1. Si")
        print("2. No")
        print("3. Salir")
        opc = int(input())
        if(opc == 1):
            info1=info()
            camper[(codigo-1)] = info1
            with open("modulos/storage/camper.json", "w") as f:
                data = json.dumps(camper, indent=4)
                f.write(data)
                f.close()
                bandera = False
        elif(opc ==2):
            bandera=False
        elif(opc == 3):
            bandera = False
    return "Edit to camper"
def eliminar():
    system("clear")
    tabla()
    print("""
                ___________________________
                * Eliminacion del camper *
                ___________________________
    """)
    codigo = int(input("Ingrese el codigo del camper que deseas actualizar: "))
    camper1(codigo)
    print("¿Este es el camper que deseas actualizar?")
    bandera=True
    while (bandera):
        print("1. Si")
        print("2. No")
        print("3. Salir")
        opc = int(input())
        if(opc == 1):
            camper.pop(codigo-1)
            with open("modulos/storage/camper.json", "w") as f:
                data = json.dumps(camper, indent=4)
                f.write(data)
                f.close()
            bandera = False'''

def mcamper():
    Ban=True
    while Ban:
        print("""
        Menu Camper
            1- Registro camper
            2- ver mis Datos
            5- Salir""")
        opc=int(input("\t"))
        match(opc):
            case(1):
                guardarcam()
            case(2):
                buscar()
            case(5):
                system("clear")
                Ban=False
            case (_):
                print("otra vez")