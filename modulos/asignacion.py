from os import system
from . import sistema ,ruta
from .sistema import continuar, guardar, traejson, listar, preingreso
import json
from .data import datos

def asignar():
    lista={"camper":{"2":"para el salto"},"trainer":{"2":"para el salto"}}
    cc="AS"+str(len(datos["asig"]))
    ruta.datos=traejson()
    ruta.tbRutas()
    codRuta=str.upper(input("Escriba el codigo de la ruta: "))
    if codRuta in datos["rutas"]:
        for i in datos["camper"]:
            if datos["camper"][i]["Estado"]=="inscrito":
                lista["camper"][i]=datos["camper"][i]
        listar("{:<15}",lista["camper"])
        cCamper=input("dijita la identificacion del camper: ")
        if cCamper in datos["camper"]:
            cTrainer=input("dijita la identificacion del Trainer: ")
            if cTrainer in datos["trainer"]:
                

    info={
        "cod_asig":cc
    }
def masignacion():
    y=True
    while y:
        print("""
        \033[1;94mMenu Asignacion\033[0m
            1- Crear asignacion
            2- Editar asignacion
            3- Eliminar asignacion
            4- Salir""")
        opc=int(input("\t"))
        system("clear")
        match(opc):
            case(1):
                asignar()
            case(2):
                editRuta()
            case(3):
                pass
            case(4):
                system("clear")
                y=False
            case (_):
                print("otra vez")