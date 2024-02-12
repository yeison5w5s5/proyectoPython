from os import system
from . import sistema ,ruta
from .sistema import continuar, guardar, traejson, listar, preingreso
import json
from .data import datos
#Valida disponibilidad del trainer devuelve trainer
def validTrainer(horario):
    lista={"0":"salto"}
    for b in datos["trainer"]:
        mal1=0
        if datos["trainer"][b]["cod_horario"][int(horario)-1]=="0" or datos["trainer"][b]["Estado"]=="pendiente":
            mal1+=1
        else:
            for b1 in datos["asig"]:
                if b == datos["asig"][b1]["cc_trainer"] and horario == datos["asig"][b1]["cod_horario"]:
                    mal1+=1
        if mal1==0:
            lista[b]=datos["trainer"][b]
    listar("{:<15}",lista)
    while True:
        cTrainer=input("dijita la identificacion del Trainer: ")
        if cTrainer not in lista:
            if continuar(2)==False:
                masignacion()
        else:
            return cTrainer
#disponibilidad de la sala de vuelve cpdigo de sala
def validSala(horario):
    lista={"0":"salto"}
    for s in dict(list(datos["salas"].items())[1:]):
        mal2=0
        for s1 in datos["asig"]:
            if datos["salas"][s]["cod_horario"][int(horario)-1]=="1":
                mal2+=1
        if mal2==0:
            lista[s]=datos["salas"][s]
    listar("{:<10}",lista)
    while True:
        cSala=str.upper(input("dijita el codigo de la sala: "))
        if cSala not in lista:
            if continuar(1)==False:
                masignacion()
        else:
            datos["salas"][cSala]["cod_horario"][int(horario)-1]="1"
            return cSala
#valida camper y devuelve lista
def validCamper(cSala,previo):
    mal=0
    lista= {"0":"salto"} if previo==[] else previo
    listacamper=[]
    for i in datos["camper"]:
        if datos["camper"][i]["Estado"]=="inscrito":
            for i1 in datos["asig"]:
                if i in datos["asig"][i1]["campers"]:
                    mal+=1
            if mal==0:
                lista[i]=datos["camper"][i]                
            mal=0
    listar("{:<15}",lista)
    while True:
        cCamper=input("dijita la identificacion del camper: ")
        if cCamper in lista:
            if (listacamper)<int(datos["Salas"][cSala]["capacidad"]):
                listacamper.append(cCamper)
            else:
                print("""
        La sala esta llena,ya no 
        puedes agregar mas campers""")
                return listacamper
            if continuar("")==False:
                return listacamper
        else:
            if continuar(1)==False:
                return listacamper
#mustra lista y devuelve codigo de ruta
def selecRuta():
    ruta.datos=traejson()
    ruta.tbRutas()
    codRuta=str.upper(input("Escriba el codigo de la ruta: "))
    if codRuta in datos["rutas"]:
        return codRuta
    else:
        selecRuta() if continuar(1)==True else  masignacion()
#Sleccion de horario devuelve codigo
def selecHorario():
    horario=input("".join([(f'{i}- {datos["horarios"][i]} \n') for i in datos["horarios"]])+"Escriba el codigo del horario: ")
    if horario in datos["horarios"]:
        return horario
    else:
        selecHorario() if continuar(1)==True else masignacion()
# Guarda datos del grupo
def guardarGrupo(cc,codRuta,horario,cTrainer,cSala,listacamper,dateini,datefin):
    info={
        "cod_asig":cc,
        "cod_ruta": codRuta,
        "cod_sala": cSala,
        "cc_trainer": cTrainer,
        "mod_actual": "1",
        "campers": listacamper,
        "inicio": dateini,
        "fin": datefin,
        "cod_horario": horario
    }
    datos["asig"][cc]=info
    sistema.datos=datos
    guardar(1)
#inprime grupo
def printgrupo(cc):
    grupo=datos["asig"][cc]
    return f"""
    ---------------gruṕo - {cc}---------------
    ruta: {grupo["cod_ruta"]} - {datos["rutas"][grupo["cod_ruta"]]["nom_ruta"]}
    sala: {grupo["cod_sala"]} - {datos["salas"][grupo["cod_sala"]]["nom_sala"]}
    trainer: {grupo["cc_trainer"]} - {datos["trainer"][grupo["cc_trainer"]]["nom_trainer"]}
    modulo actual: {grupo["mod_actual"]}
    campers: {len(grupo["campers"])}
    fecha: inicio > {grupo["inicio"]} - fin > {grupo["fin"]}
    horario: {datos["horarios"][grupo["cod_horario"]]}
    -------------------------------------------"""
#pregunta para continuar
def pregunta():
    print("\t^ Editaras esto ^")
    return continuar("")
#menu edicon asig
def editasig(cc):
    codRuta=""
    grupo=datos["asig"][cc]
    horario=grupo["cod_horario"]
    print(f'\truta: {grupo["cod_ruta"]} - {datos["rutas"][grupo["cod_ruta"]]["nom_ruta"]}')
    codRuta= selecRuta() if pregunta()==True else grupo["cod_ruta"]
    print(f'\tsala: {grupo["cod_sala"]} - {datos["salas"][grupo["cod_sala"]]["nom_sala"]}')
    cSala= validSala(horario) if pregunta()==True else grupo["cod_sala"]
    print(f'\ttrainer: {grupo["cc_trainer"]} - {datos["trainer"][grupo["cc_trainer"]]["nom_trainer"]}')
    cTrainer= validTrainer(horario) if pregunta()==True else grupo["cc_trainer"]
    print(f'\tfecha: inicio > {grupo["inicio"]} - fin > {grupo["fin"]}')
    dateini,datefin = [grupo["inicio"], grupo["fin"]] if pregunta()==False else [input("\tIngresa la fecha de inicion es el siguiente formato: (dd-mm-aaaa): "),input("\tIngresa la fecha de finalizacion es el siguiente formato: (dd-mm-aaaa): ")]
    guardarGrupo(cc,codRuta,grupo["cod_horario"],cTrainer,cSala,grupo["campers"],dateini,datefin)
#lista los campers en el grupo
def campergrup(cc):
    lista={"0":"0"}
    for i in datos["asig"][cc]["campers"]:
        lista[i]=datos["camper"][i]
    listar("{:<15}",lista)
#menu edicon de campers en el grupo
def editcamper(cc):
    grupo=datos["asig"][cc]
    print("""
        --- Edicion de campers ---
          1. Agregar Campers    
          2. Eliminar Campers
          3. Salir
""")
    while True:
        opc=input(": ")
        match(opc):
            case "1":
                print("-------los campers en grupo---------")
                campergrup(cc)
                print("-------los campers que puedes agregar---------")
                lista=validCamper(grupo["cod_horario"],grupo["campers"])
                for i in lista:
                    datos["asig"][cc]["campers"].append(i)
                sistema.datos=datos
                guardar(1)
                break
            case "2":
                print("-------los campers en grupo---------")
                campergrup(cc)
                while True:
                    cCamper=input("Escriba el numero de identificaion del camper que quiere eliminar: ")
                    if cCamper in  datos["asig"][cc]["campers"]:   
                        datos["asig"][cc]["campers"].remove(cCamper)
                        sistema.datos=datos
                        guardar(2)
                        if continuar("")==False:
                            break 
                    else:
                        Editgrupo() if continuar(1)==False else editcamper(cc)
                    
                        
                break
            case "3":
                masignacion()
#Edicion del grupo
def Editgrupo():
    for i in datos["asig"]:
        print(printgrupo(i))
    cc=str.upper(input("Esbribe el codigo del grupo a editar: "))
    if cc not in datos["asig"]:
        Editgrupo() if continuar(1)==True else masignacion()
    else:
        print(printgrupo(cc))
        print("\n\t\tEste es el grupo que quieres editar?")
        if continuar("")==False:
            masignacion()
        else:
            while True:
                print("""
        ------Menu de edicon de Grupo------
            1- modificar datos
            2- modificar campers
            3- Salir
        -----------------------------------""")
                opc=input(": ")
                match (opc):
                    case "1":
                        editasig(cc)
                    case "2":
                        editcamper(cc)
                    case "3":
                        masignacion()
                    case _:
                        print("\tOpcion no valida")
#crear grupo
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
    listacamper=validCamper(cSala,[])
#fecha inicio y fin
    dateini=input("Ingresa la fecha de inicion es el siguiente formato: (dd-mm-aaaa): ")
    datefin=input("Ingresa la fecha de finalizacion es el siguiente formato: (dd-mm-aaaa): ")      
#guardar grupo
    guardarGrupo(cc,codRuta,horario,cTrainer,cSala,listacamper,dateini,datefin)

def delAsig():
    for i in datos["asig"]:
        print(printgrupo(i))
    cc=str.upper(input("Esbribe el codigo del grupo a eliminar: "))
    if cc not in datos["asig"]:
        ("Codigo no identificado")
    else:
        print(printgrupo(cc))
        print("\n\t\tEste es el grupo que quieres Eliminar?")
        if continuar("")==False:
            masignacion()
        else:
            datos["asig"].pop(cc)
            sistema.datos=datos
            guardar(2)

def masignacion():
    y=True
    while y:
        print("""
        \033[1;94mMenu Asignacion\033[0m
            1- Crear Grupo
            2- Editar Grupo
            3- Eliminar asignacion
            4- Salir""")
        opc=input("\t")
        system("clear")
        match(opc):
            case("1"):
                asignar()
            case("2"):
                Editgrupo()
            case("3"):
                delAsig()
            case("4"):
                system("python3 main.py")
            case (_):
                print("otra vez")