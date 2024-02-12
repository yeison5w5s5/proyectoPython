from os import system
import json
from .data import datos
from .sistema import continuar, guardar, traejson, numeros
from . import sistema
from datetime import date
def prueba(codigo):
    logica = 0
    programacion = 0
    #Prueba proporcionada por gpto
    # Pregunta 1: Lógica
    print("1. ¿Cuál de las siguientes afirmaciones lógicas es verdadera?")
    print("A. True AND False")
    print("B. True OR False")
    print("C. NOT True")
    respuesta_1 = str.upper(input("Tu respuesta (A, B o C): "))

    if respuesta_1 == "B":
        logica += 10

    # Pregunta 2: Programación básica
    print("\n2. ¿Qué función se utiliza para imprimir en la consola en Python?")
    print("A. print()")
    print("B. display()")
    print("C. show()")
    respuesta_2 = str.upper(input("Tu respuesta (A, B o C): "))

    if respuesta_2 == "A":
       programacion += 10

    # Pregunta 3: Lógica
    print("\n3. ¿Cuál es el resultado de la expresión (True AND False) OR True?")
    print("A. True")
    print("B. False")
    print("C. Error")
    respuesta_3 = str.upper(input("Tu respuesta (A, B o C): "))

    if respuesta_3 == "A":
        logica += 10

    # Pregunta 4: Programación básica
    print("\n4. ¿Cómo se inicia un comentario de una línea en Python?")
    print("A. // Comentario")
    print("B. /* Comentario */")
    print("C. # Comentario")
    respuesta_4 = str.upper(input("Tu respuesta (A, B o C): "))

    if respuesta_4 == "C":
       programacion += 10

    # Pregunta 5: Lógica
    print("\n5. ¿Cuál es el resultado de la expresión NOT (True AND False)?")
    print("A. True")
    print("B. False")
    print("C. Error")
    respuesta_5 = str.upper(input("Tu respuesta (A, B o C): "))

    if respuesta_5 == "A":
        logica += 10

    # Pregunta 6: Programación básica
    print("\n6. ¿Qué función se utiliza para obtener la longitud de una lista en Python?")
    print("A. size()")
    print("B. length()")
    print("C. len()")
    respuesta_6 = str.upper(input("Tu respuesta (A, B o C): "))

    if respuesta_6 == "C":
       programacion += 10

    # Pregunta 7: Lógica
    print("\n7. ¿Cuál es la salida de la operación 3 ^ 2?")
    print("A. 6")
    print("B. 9")
    print("C. 5")
    respuesta_7 = str.upper(input("Tu respuesta (A, B o C): "))

    if respuesta_7 == "B":
        logica += 10

    # Pregunta 8: Programación básica
    print("\n8. ¿Cómo se declara una variable en Python?")
    print("A. variable x")
    print("B. x = variable")
    print("C. x = 5")
    respuesta_8 = str.upper(input("Tu respuesta (A, B o C): "))

    if respuesta_8 == "C":
       programacion += 10

    # Pregunta 9: Lógica
    print("\n9. ¿Cuál es el resultado de la expresión (False OR True) AND False?")
    print("A. True")
    print("B. False")
    print("C. Error")
    respuesta_9 = str.upper(input("Tu respuesta (A, B o C): "))

    if respuesta_9 == "B":
        logica += 10

    # Pregunta 10: Programación básica
    print("\n10. ¿Qué operador se utiliza para calcular el residuo de una división en Python?")
    print("A. %")
    print("B. /")
    print("C. //")
    respuesta_10 = str.upper(input("Tu respuesta (A, B o C): "))

    if respuesta_10 == "A":
       programacion += 10

    # Mostrar resultados
    promedio=logica+programacion/2
    print(f"""
        Puntaje de lógica: {logica}
        Puntaje de programación:   {programacion}
        promedio: {promedio}""")
    datos["pruebas"][codigo]={"cc_camper":codigo,
                                         "logica":logica,
                                         "tecnico":programacion,
                                         "promedio":promedio,
                                         "Fecha:": date.today()}
    if promedio>60:
        datos["camper"][codigo]["Estado"]="inscrito"
        print("Felicidades, haz aprobado")
    else:
        print("Intentalo el otro año xD")
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
    cc=numeros("Ingrese numero de identificacion: ")
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
            5- Salir""")
        opc=input("\t")
        match(opc):
            case("1"):
                guardarcam()
            case("2"):
                buscar()
            case("5"):
                system("python3 main.py")
            case (_):
                print("otra vez")