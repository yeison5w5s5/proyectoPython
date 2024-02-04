from os import system
import json
from .data import datos

def guardar():
    with open("modulos/storage/data.json", "w") as f:
        data=json.dumps(datos, indent=4)
        f.write(data)
        f.close()

def info(cc):
    data={
        "cc_camper":cc,
        "nom_camper":str.upper(input("Ingrese su nombre: ")),
        "apell_camper":str.upper(input("Ingrese su apellido: ")),
        "edad_camper":int(input("Ingrese su edad: ")),
        "Dirr_camper":str.upper(input("Ingrese su direccion: ")),
        "Estado":"preinscrito",
        "cc_acudi":int(input("Ingrse numnero de identifiacion del acudiente: ")),
        "nom_acudiente":str.upper(input("Ingrse nombre completo de su acudiente: ")),
    }
    return data

def guardarcam():
    cc=int(input("Ingrese numero de identificacion: "))
    if str(cc) in datos["camper"]:
        print("Este numero ya existe")
        guardarcam()
    else:
        datos["camper"][cc]=info(cc)
        guardar()
    return "Sucessfully Camper"    
def buscar():
    system("clear")
    return "The camper is available"
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
            1- Guardar camper
            2- Buscar Camper
            3- Editar Camper
            4- Eliminar Camper
            5- Salir""")
        opc=int(input("\t"))
        match(opc):
            case(1):
                guardarcam()
            case(2):
                buscar()
            case(3):
                editar()
            case(4):
                eliminar()
            case(5):
                system("clear")
                Ban=False
            case (_):
                print("otra vez")