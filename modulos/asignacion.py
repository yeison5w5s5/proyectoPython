from os import system
from . import sistema ,ruta
from .sistema import continuar, guardar, traejson, listar, preingreso
import json
from .data import datos

def validTrainer(horario):
    lista={"0":"salto"}
    for b in datos["trainer"]:
        mal1=0
        if datos["trainer"][b]["cod_horaio"][int(horario)-1]=="0" or datos["trainer"][b]["Estado"]=="pendiente":
            mal1+=1
        else:
            for b1 in datos["asig"]:
                if b == datos["asig"][b1]["cc_trainer"] and horario == datos["asig"][b1]["cod_horaio"]:
                    mal1+=1
        if mal1==0:
            lista[b]=datos["trainer"][b]
    listar("{:<15}",lista)
    while True:
        cTrainer=input("dijita la identificacion del Trainer: ")
        if cTrainer not in datos["trainer"]:
            print("Codigo no identificado o trainer no disponible")
            if continuar()==False:
                masignacion()
        else:
            return(cTrainer)

def validSala(horario):
    lista={"0":"salto"}
    for s in dict(list(datos["salas"].items())[1:]):
        mal2=0
        for s1 in datos["asig"]:
            if datos["salas"][s]["cod_horaio"][int(horario)-1]=="1":
                mal2+=1
        if mal2==0:
            lista[s]=datos["salas"][s]
    listar("{:<10}",lista)
    while True:
        cSala=str.upper(input("dijita el codigo de la sala: "))
        if cSala not in lista:
            print("Codigo no identificado o sala no disponible")
            if continuar()==False:
                masignacion()
        else:
            datos["salas"][cSala]["cod_horaio"][int(horario)-1]="1"
            return cSala

def validCamper():
    lista={"0":"salto"}
    listacamper=[]
    for i in datos["camper"]:
        if datos["camper"][i]["Estado"]=="preinscrito":
            for i1 in datos["asig"]:
                if i in datos["asig"][i1]["campers"]:
                    mal+=1
                    print(mal)
            if mal==0:
                lista[i]=datos["camper"][i]                
            mal=0
    listar("{:<17}",lista)
    while True:
        cCamper=input("dijita la identificacion del camper: ")
        if cCamper in lista:
            listacamper.append(cCamper)
        else:
            print("cc no identificado o no disponible")
        if continuar()==False:
            return listacamper

def selecRuta():
    ruta.datos=traejson()
    ruta.tbRutas()
    codRuta=str.upper(input("Escriba el codigo de la ruta: "))
    if codRuta in datos["rutas"]:
        return codRuta
    else:
        selecRuta() if continuar==True else  masignacion()

def selecHorario():
    horario=input("".join([(f'{i}- {datos["horarios"][i]} \n') for i in datos["horarios"]])+"Escriba el codigo del horario: ")
    if horario in datos["horarios"]:
        return horario
    else:
        selecHorario() if continuar==True else masignacion()

def guardarGrupo(cc,codRuta,horario,cTrainer,cSala,listacamper,dateini,datefin):
    info={
        "cod_asig":cc,
        "cod_ruta": codRuta,
        "cod_sala": cSala,
        "cc_trainer": cTrainer,
        "campers": listacamper,
        "inicio": dateini,
        "fin": datefin,
        "cod_horaio": horario
    }
    datos["asig"][cc]=info
    sistema.datos=datos
    guardar(1)

def asignar():
    cTrainer=""
    cSala=""
    listacamper=[]
    cc="M"+str(len(datos["asig"]))
#eleccion de rutas de rutas
    codRuta=selecRuta()
#elecion de horario
    horario=selecHorario()
#eleccion de Trainer
    cTrainer=validTrainer(horario)
#eleccion de rutas de Salas
    cSala=validSala(horario)
#eleccion de rutas de campers
    listacamper=validCamper()
#fecha inicio y fin
    dateini=input("Ingresa la fecha de inicion es el siguiente formato: (dd-mm-aaaa): ")
    datefin=input("Ingresa la fecha de finalizacion es el siguiente formato: (dd-mm-aaaa): ")      
#guardar grupo
    guardarGrupo(cc,codRuta,horario,cTrainer,cSala,listacamper,dateini,datefin)

def masignacion():
    y=True
    while y:
        print("""
        \033[1;94mMenu Asignacion\033[0m
            1- Crear Grupo
            2- Editar Grupo
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