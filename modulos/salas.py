from os import system
from . import sistema
from .sistema import continuar, guardar, traejson, listar, preingreso
import json
from .data import datos

def crear(a):
    b,c,cod= ["","",("S0"+str((datos["salas"]["cont"])))] if a=="" else [a["nom_sala"],a["capacidad"],a["cod_sala"]]
    data={
        "cod_sala":cod,
        "nom_sala":preingreso("ingrese el nombre de la sala: ",b),
        "capacidad":preingreso("Ingrese la capacidad de la sala: ",c),
        "cod_horaio": [
                "0",
                "0",
                "0",
                "0"
            ]
    }
    datos["salas"][cod]=data
    datos["salas"]["cont"]+=1 if a=="" else datos["salas"]["cont"] 
    sistema.datos=datos
    guardar(1)

def editar(a):
    listar("{:<15}",datos["salas"])
    cod=str.upper(input("\n Escribe el codigo de la Sala: "))
    if cod in datos["salas"]:
        sala=datos["salas"][cod]
        print(f"""
    _________________________
    codigo- {sala["cod_sala"]}
    nombre- {sala["nom_sala"]}
    capacidad- {sala["capacidad"]}
    -------------------------
       Esta es tu sala?
    """)
        if continuar("")==True:
            if a==1:
                crear(sala) 
            else:
                datos["salas"].pop(cod)
                sistema.datos=datos
                guardar(2)
        else:
            msalas()
    else:
        editar() if continuar(1)==True else msalas()



def msalas():
    datos=traejson
    x=True
    while x:
        print("""
        \033[1;94mMenu Salas\033[0m
            1- Crear
            2- Editar
            3- Eliminar
            4- Listar
            5- Salir""")
        opc=input("\t")
        system("clear")
        match(opc):
            case("1"):
                crear("")
            case("2"):
                editar(1)
            case("3"):
                editar(2)
            case("4"):
                listar("{:<15}",traejson()["salas"])
            case("5"):
                system("python3 main.py")
            case (_):
                print("otra vez")