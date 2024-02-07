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
        horario=input("".join([(f'{i}- {datos["horarios"][i]} \n') for i in datos["horarios"]])+"Escriba el codigo del usuario: ")
        if horario in datos["horarios"]:
            for i in datos["camper"]:
                if datos["camper"][i]["Estado"]=="preinscrito":
                    for i1 in datos["asig"]:
                        if datos["camper"][i] not in datos["asig"][i1]["campers"]:
                            lista["camper"][i]=datos["camper"][i]
            listar("{:<15}",lista["camper"])
            listacamper=[]
            while True:
                cCamper=input("dijita la identificacion del camper: ")
                if cCamper in lista["camper"]:
                    listacamper.append(cCamper)
                else:
                    print("cc no identificado o no disponible")
                if continuar()==False:
                    break
            for b in datos["trainer"]:
                if datos["trainer"][b]["cod_horaio"][int(horario)-1]=="1" and datos["trainer"][b]["Estado"]=="contratado":
                    for b1 in datos["asig"]:
                        if datos["trainer"][b] not in datos["asig"][b1]["cc_trainer"] and horario != datos["asig"][b1]["cod_horaio"]:
                            lista["trainer"][b]=datos["trainer"][b]
            listar("{:<15}",lista["trainer"])
            cTrainer=input("dijita la identificacion del Trainer: ")
            if cTrainer in datos["trainer"]:
                pass
                    
                

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