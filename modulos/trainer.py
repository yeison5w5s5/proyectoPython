from os import system
import json

def info():
    data={
        "cc_trainer":int(input("Ingrese numerpo de identificacion: ")),
        "nom_trainer":str.upper(input("Ingrese su nombre: ")),
        "cod_horaio":0,
        "cod_ruta":0
    }
    return data