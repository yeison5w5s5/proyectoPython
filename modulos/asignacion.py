from os import system
from . import sistema ,ruta
from .sistema import continuar, guardar, traejson, listar, preingreso
import json
from .data import datos

def asignar():
    mal=0
    cTrainer=""
    cSala=""
    listacamper=[]
    lista={"camper":{"0":"para el salto"},"trainer":{"0":"para el salto"},"salas":{"0":"para salto"}}
    cc="AS"+str(len(datos["asig"]))
    ruta.datos=traejson()
    ruta.tbRutas()
    codRuta=str.upper(input("Escriba el codigo de la ruta: "))
    if codRuta in datos["rutas"]:
        horario=input("".join([(f'{i}- {datos["horarios"][i]} \n') for i in datos["horarios"]])+"Escriba el codigo del horario: ")
        if horario in datos["horarios"]:
            for b in datos["trainer"]:
                mal1=0
                if datos["trainer"][b]["cod_horaio"][int(horario)-1]=="0" or datos["trainer"][b]["Estado"]=="pendiente":
                    mal1+=1
                else:
                    for b1 in datos["asig"]:
                        if b == datos["asig"][b1]["cc_trainer"] and horario == datos["asig"][b1]["cod_horaio"]:
                            mal1+=1
                if mal1==0:
                    lista["trainer"][b]=datos["trainer"][b]
            listar("{:<15}",lista["trainer"])
            while True:
                cTrainer=input("dijita la identificacion del Trainer: ")
                if cTrainer not in datos["trainer"]:
                    print("Codigo no identificado o trainer no disponible")
                    if continuar()==False:
                        masignacion()
                else:
                    break
            for s in dict(list(datos["salas"].items())[1:]):
                mal2=0
                for s1 in datos["asig"]:
                    if datos["salas"][s]["cod_horaio"][int(horario)-1]=="1":
                        mal2+=1
                if mal2==0:
                    lista["salas"][s]=datos["salas"][s]
            listar("{:<10}",lista["salas"])
            while True:
                cSala=str.upper(input("dijita el codigo de la sala: "))
                if cSala not in datos["salas"]:
                    print("Codigo no identificado o sala no disponible")
                    if continuar()==False:
                        masignacion()
                else:
                    break
            for i in datos["camper"]:
                if datos["camper"][i]["Estado"]=="preinscrito":
                    for i1 in datos["asig"]:
                        if i in datos["asig"][i1]["campers"]:
                            mal+=1
                            print(mal)
                    if mal==0:
                        lista["camper"][i]=datos["camper"][i]                
                    mal=0
            listar("{:<17}",lista["camper"])
            while True:
                cCamper=input("dijita la identificacion del camper: ")
                if cCamper in lista["camper"]:
                    listacamper.append(cCamper)
                else:
                    print("cc no identificado o no disponible")
                if continuar()==False:
                    break
            dateini=input("Ingresa la fecha de inicion es el siguiente formato: (dd-mm-aaaa): ")
            datefin=input("Ingresa la fecha de finalizacion es el siguiente formato: (dd-mm-aaaa): ")
                    
                

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