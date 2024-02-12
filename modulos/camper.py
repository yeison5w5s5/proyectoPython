from os import system
import json
from .data import datos
from .sistema import continuar, guardar, traejson, numeros, enteros
from . import sistema
from datetime import date
def prueba(codigo):
    logica = numeros("ingrese el puntaje de Practico: ")
    programacion = numeros("ingrese su puntaje teorico: ")
    
    promedio=(logica+programacion)/2
    fecha= date.today()
    fecha=str(fecha)
    print(f"""
        Puntaje de lógica: {logica}
        Puntaje de programación:   {programacion}
        promedio: {promedio}""")
    datacamp={"cc_camper":codigo,
        "practica":logica,
        "teorica":programacion,
        "promedio":("{0:.1f}".format(promedio)),
        "Fecha:": fecha}
    if promedio>60:
        datos["camper"][codigo]["Estado"]="inscrito"
        print("Felicidades, haz aprobado")
    else:
        datos["camper"][codigo]["Estado"]="reprobado"
        print("Intentalo el otro año xD")
    datos["pruebas"][codigo]=datacamp
    sistema.datos=datos
    guardar(1)
    mcamper()

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
    cc=enteros("Ingrese numero de identificacion: ")
    if str(cc) in datos["camper"]:
        print("Este numero ya existe")
        guardarcam()
    else:
        datos["camper"][str(cc)]=info(cc)
        sistema.datos=datos
        guardar(1)
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
        if datos["camper"][codigo]["Estado"]=="preinscrito":
            print("""
            aun no haz realizado la prueba 
            de admision, quieres realizarla?""")
            prueba(codigo) if continuar("")==True else mcamper()
    else:
        if continuar("")==True:
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
            0- Salir""")
        opc=input("\t")
        match(opc):
            case("1"):
                guardarcam()
            case("2"):
                buscar()
            case("0"):
                system("python3 main.py")
            case (_):
                print("otra vez")