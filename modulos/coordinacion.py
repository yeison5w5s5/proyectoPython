from os import system
import json
import readline
from .sistema import continuar
from .data import datos

def traejson():
    system("clear")
    with open("modulos/storage/data.json", "r") as f:
                datos=json.loads(f.read())
                f.close()
                return datos
def guardar():
    with open("modulos/storage/data.json", "w") as f:
        data=json.dumps(datos, indent=4)
        f.write(data)
        f.close()
    datos=traejson()

def preingreso(mensaje, valor_predeterminado):
    readline.set_startup_hook(lambda: readline.insert_text(valor_predeterminado))
    try:
        entrada_usuario = input(f'{mensaje}')
    finally:
        readline.set_startup_hook()
    return entrada_usuario

def tbMod(i):    
    for b in i["modulos"]:
        print(f"""
            -{b}-{i["modulos"][b]["nom_mod"]}-
            nombre: {i["modulos"][b]["nom_mod"]}
            Temario: {"".join([f"{c} - " for c in i["modulos"][b]["temario"]])}""")
def tbRuta(i):
    ruta=datos["rutas"][i]
    print(f"""
            ________________________________________
               -codigo- {i}  -nombre- {ruta["nom_ruta"]}   
            ---------------Modulos------------------""")
    tbMod(ruta)
def tbRutas():
    for i in datos["rutas"]:
        tbRuta(i)
        


def mcoordi():
    x=True
    while x:
        print("""
        \033[1;94mMenu Coordinacion\033[0m
            1- Configurar Rutas
            2- 
            3- 
            4- 
            5- Salir""")
        opc=int(input("\t"))
        system("clear")
        match(opc):
            case(1):
                menurutas()
            case(2):
                pass
            case(3):
                pass
            case(4):
                pass
            case(5):
                x=False
            case (_):
                print("otra vez")


def modulos(codigo):
    lista=datos["rutas"][str(codigo)]["modulos"] if codigo!="" else {}
    print(lista)
    x=True
    while x:
        codigo=input("Ingresa el codigo del modulo: ")
        if codigo in lista:
            print("\033[1;33mYa hay un modulo con este codigo\033[0m")
        else:
            modulo={
                "cod_mod":codigo,
                "nom_mod":str(input("Ingresa el nombre del modulo: ")),
                "temario":[str(input(f"ingrese el temario {i+1}: "))for i in range(int(input("Defina la cantidad de datos: ")))]
            }
            lista[str(codigo)]=modulo
        x=continuar()
    return lista

def rutas(codigo):
    data={
        "cod_ruta":codigo,
        "nom_ruta":str(input("ingrese el nombre de la ruta: ")),
        "modulos":modulos("")
    }
    datos["rutas"][str(codigo)]=data
    guardar()
    return "Ruta Guardada"

def editRuta():
    while True:
        tbRutas()
        codigo=input("Ingresa el codigo de la ruta a editar: ")
        if codigo in datos["rutas"]:
            tbRuta(codigo)
            if continuar==False:
                break
            print("""
                \033[1;94mMenu de edicion de ruta\033[0m
                1- Editar Ruta
                2- Agregar modulos
                3- Rehacer ruta""")
            opc=int(input())
            match(opc):
                case(1):
                    rutas(codigo)
                case(2):
                    modulos(codigo)
                    guardar()

        else:
            print("No se encontro ruta con este codigo")
            if continuar()==False:
                break


def menurutas():
    y=True
    while y:
        print("""
        \033[1;94mMenu Rutas\033[0m
            1- Crear ruta
            2- Editar rutas
            3- Asignar rutas
            4- Eliminar Camper
            5- Salir""")
        opc=int(input("\t"))
        system("clear")
        match(opc):
            case(1):
                def prueba():
                    codigo=input("ingrese el codigo de la ruta:")
                    if codigo in datos["rutas"]:
                        print("\033[1;33mYa hay una ruta con este codigo\033[0m")
                        return "bye" if continuar()==False else prueba()
                    else:
                        rutas(codigo)
                prueba()
            case(2):
                editRuta()
            case(3):
                pass
            case(4):
                pass
            case(5):
                system("clear")
                y=False
            case (_):
                print("otra vez")