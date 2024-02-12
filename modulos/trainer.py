from os import system
from .data import datos
from .sistema import continuar, guardar, numeros, listar
from . import sistema, asignacion
import json

def login():
    cTrainer= input("ingresa tu numero de identificacion: ")
    if cTrainer not in datos["trainer"]:
        login() if continuar(2)==True else mtrainer()
    else:
        opcTrainer(cTrainer)

def notasCampers(cGrupo,cTrainer):
    if cGrupo=="":
        grupos=verGrupo(cTrainer)
        if grupos==[]:
            opcTrainer(cTrainer)
        else:
            while True:
                cGrupo= str.upper(input("ingresa el codigo del grupo que quieres ver: "))
                if cGrupo not in grupos:
                    opcTrainer(cTrainer) if continuar(1)==False else print("otra vez")
                else:
                    print(asignacion.printgrupo(cGrupo))
                    break
    grupo=datos["asig"][cGrupo]
    for camper in grupo["campers"]:
        lista={"0":"0"}
        info={}
        datacamper=datos["camper"][camper]
        info={
                "CC_camper":camper,
                "Nombre": datacamper["nom_camper"],
                "Apellido":datacamper["apell_camper"],
                "Estado":datacamper["Estado"]
            }
        lista[camper]=info
        listar("{:<10}",lista)
        lista={"0":"0"}
        print("\t\t-------Notas-------")
        for i in datos["notas"][cGrupo]:
            if datos["notas"][cGrupo][i]=={}:
                pass
            else:
                notas= datos["notas"][cGrupo][i][camper]
                info={
                    "modulo":i,
                    "Teorioca":notas["teorica"],
                    "Practica":notas["practica"],
                    "Quices":notas["quices"],
                    "Final":notas["nota_ finals"],
                    "Desicion":notas["desicion"]
                }
                lista[i]=info
        listar("{:<10}",lista)
        print("\033[1;94m------------------------------------------------------------------------------\033[0m\n")

    opcTrainer(cTrainer)

def verGrupo(cTrainer):
    grupos=[]
    for i in datos["asig"]:
        if datos["asig"][i]["cc_trainer"]==cTrainer:
            asignacion.datos=datos
            print(asignacion.printgrupo(i))
            grupos.append(i)
    if grupos==[]:
        print("aun no tienes grupos asignados")
    return grupos

def ponernotas(cTrainer):
    grupos=verGrupo(cTrainer)
    if grupos!=[]:
        while True:
            cGrupo= str.upper(input("ingresa el codigo del grupo que quieres ver: "))
            if cGrupo not in grupos:
                opcTrainer(cTrainer) if continuar(1)==False else print("otra vez")
            else:
                break
        grupo=datos["asig"][cGrupo]
        print(asignacion.printgrupo(cGrupo))
        print(f"""
Su grupo esta en el modulo {grupo["mod_actual"]}
si ya termino puede ingresar las notas de 
sus campers
        """)
        if continuar("")==False:
            login()
        else:
            if grupo["mod_actual"]=="1":
                print("creando primero")
                datos["notas"][cGrupo]={"Mod1":{},"Mod2":{},"Mod3":{},"Mod4":{},"Mod5":{}}
            for camper in grupo["campers"]:
                if datos["camper"][camper]["Estado"]!="Reprobado":
                    print(f"""
identificacion:{camper} nombre: {datos["camper"][camper]["nom_camper"]} {datos["camper"][camper]["apell_camper"]}
""")
                    notapt=numeros("\t\t Ingrese la nota de la prueba teorica: ")
                    notapp=numeros("\t\t Ingrese la nota de la prueba practica: ")
                    qses=numeros("\t\t Ingrese la nota total de quices: ")
                    promedio= notapt*0.3+notapp*0.6+qses*0.1
                    desicion=""

                    if promedio>60:
                        desicion="Aprobo"
                        if (grupo["mod_actual"]=="1" or grupo["mod_actual"]=="5"):
                            datos["camper"][camper]["Estado"]="aprobado"
                    else:
                        desicion="reprobo"
                        if datos["camper"][camper]["Estado"]=="Enriesgo":
                            print("\t\tEste camper ha reprobado")
                            datos["camper"][camper]["Estado"]="Reprobado"
                        else:
                            datos["camper"][camper]["Estado"]="Enriesgo"
                    info={
                        "teorica":notapt,
                        "practica":notapp,
                        "quices":qses,
                        "nota_ finals":"{0:.1f}".format(promedio),
                        "desicion":desicion
                    }
                    datos["notas"][cGrupo]["Mod"+grupo["mod_actual"]][camper]=info
            datos["asig"][cGrupo]["mod_actual"]=str(int(grupo["mod_actual"])+1)
            sistema.datos=datos
            guardar(1)
            notasCampers(cGrupo,cTrainer)

def info():
    cc=numeros("ingresa tu numero de  ID: ")
    if str(cc) in datos["trainer"]:
        print("Este numero ya existe")
        info()
    else:
        nombre=str.upper(input("Ingrese su nombre: "))
        print("""
            Para elegir el horario dijita 
                1=disponible
                0=no disponible
            Frente a cada horario""")
        data={
            "cc_trainer":cc,
            "nom_trainer":nombre,
            "cod_horario":[input(f'\n{i}- {datos["horarios"][i]}: ') for i in datos["horarios"]],
            "Estado":"pendiente"
        }
        datos["trainer"][cc]=data
        sistema.datos=datos
        guardar(1)
    return data

def opcTrainer(cTrainer):
    trainer=datos["trainer"][cTrainer]
    while True:
        print(f"""
    --------Opciones del trainer---------
        CC: {cTrainer} nombre: {trainer["nom_trainer"]}

            1- ver mis grupos
            2- Poner notas
            3- Ver notas
            4- Salir
        """)
        opc=input(": ")
        match opc:
            case "1":
                verGrupo(cTrainer)
            case "2":
                ponernotas(cTrainer)
            case "3":
                notasCampers("",cTrainer)
            case "4":
                mtrainer()
            case _:
                print("codigo no identificado")

def mtrainer():
    y=True
    while y:
        print("""
        \033[1;94mMenu Trainer\033[0m
            1- Registro
            2- Ingreso
            3- Salir""")
        opc=input("\t")
        system("clear")
        match(opc):
            case("1"):
                info()
            case("2"):
                login()
            case("3"):
                system("python3 main.py")
            case (_):
                print("otra vez")