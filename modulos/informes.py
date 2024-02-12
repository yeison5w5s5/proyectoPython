from .sistema import listar
from .data import datos
from . import sistema, coordinacion, asignacion
from os import system

def informe1():
    system("clear")
    lista= {"0":"salto"}
    for i in datos["camper"]:
        if datos["camper"][i]["Estado"]=="inscrito":
                lista[i]=datos["camper"][i]                

    listar("{:<15}",lista)

def informe2():
    lista={"20":"2"}
    for i in datos["camper"]:
        camper=datos["camper"][i]
        if i in datos["pruebas"]:
            prueba=datos["pruebas"][i]
            if prueba["promedio"]>60:
                info={
                    "CC": i,
                    "Nombre": camper["nom_camper"],
                    "Apellido": camper["apell_camper"],
                    "Practica": prueba["practica"],
                    "Teorica": prueba["teorica"],
                    "Promedio": prueba["promedio"]
                }
                lista[i]=info
    listar("{:<13}",lista)

def informe3():
    lista={"0":"salto"}
    for b in datos["trainer"]:
        trainer=datos["trainer"][b]
        if trainer["Estado"]=="contratado":
             lista[b]=trainer
    listar("{:<13}",lista)

def informe4():
    system("clear")
    lista= {"0":"salto"}
    for i in datos["camper"]:
        if datos["camper"][i]["Estado"]=="Enriesgo":
                lista[i]=datos["camper"][i]                

    listar("{:<15}",lista)

def informe5():
    for i in datos["asig"]:
        asignacion.datos=datos
        grupo=datos["asig"][i]
        print(asignacion.printgrupo(i))
        lista= {"0":"salto"}
        for i in grupo["campers"]:
            camper=datos["camper"][i]
            info={
                "cc":i,
                "nombre":camper["nom_camper"],
                "apellido":camper["apell_camper"],
            }
            lista[i]=info
        listar("{:<15}",lista)

def informe6():
    for i in datos["asig"]:
        cGrupo=i
        asignacion.datos=datos
        print(asignacion.printgrupo(i))
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
            if cGrupo in datos["notas"]:
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

def minformes():
    while True:   
        print(f"""
    ------------------------------menu informes-------------------------------
        
        1- Listar los campers que se encuentren en estado de inscrito.
        
        2- Listar los campers que aprobaron el examen inicial.
        
        3- Listar los entrenadores que se encuentran trabajando con campuslands.
        
        4- Listar los estudiantes que cuentan con bajo rendimiento.
        
        5- Listar los campers y entrenador que se encuentren asociados a una 
        ruta de entrenamiento.
        
        6- Mostrar cuantos campers perdieron y aprobaron cada uno de los modulos 
        teniendo en cuenta la ruta de entrenamiento y el entrenador encargado.
        
        0- Salir""")
        opc=input(": ")
        match opc:
            case "1":
                  informe1()
            case "2":
                  informe2()
            case "3":
                  informe3()
            case "4":
                  informe4()
            case "5":
                  informe5()
            case "6":
                  informe6()
            case "0":
                  coordinacion.mcoordi()

