
from os import system
import readline
import json
from .data import datos
def continuar(a):
    X=True
    while True:
        if a==1:
            print("\t\tCodigo no identificado")
        elif a==2:
            print("\t\tNumero no identificado")
        else: 
            pass
        print("""
            ¿Quieres continuar?
                1=Si
                2=No""")
        opc=input("")
        match(opc):
            case("1"):
                x=True
                break
            case("2"):
                x=False
                break
            case(_):
                print("opcion no disponible")
    return x

def guardar(a):
    with open("modulos/storage/data.json", "w") as f:
        data=json.dumps(datos, indent=4)
        f.write(data)
        f.close()
    
    print("\t\033[1;32mguardado\033[0m") if a==1 else print("\t\033[1;31mEliminado\033[0m")
    
def traejson():
    system("clear")
    with open("modulos/storage/data.json", "r") as f:
                datos=json.loads(f.read())
                f.close()
                return datos

def preingreso(mensaje, valor_predeterminado):
    readline.set_startup_hook(lambda: readline.insert_text(valor_predeterminado))
    try:
        entrada_usuario = input(f'{mensaje}')
    finally:
        readline.set_startup_hook()
    return entrada_usuario

def listar(a,x):
    for i in dict(list(x.items())[1:]):
        for v in x[i]:
            print( "\033[44m",a.format(v),"\033[0","\033[1;94m║\033[0m" ,end="")
        print(flush=0)
        break
    for i in dict(list(x.items())[1:]):
        for v in x[i]:
            print("",a.format(str(x[i][v]),),"\033[1;94m║\033[0m",end="")
        print(flush=0)

def numeros(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor solo ingresa numeros")

def enteros(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor solo ingresa numeros")