from os import system
import json

def info():
    data={
        "cc_camper":int(input("Ingrese numerpo de identificacion: ")),
        "nom_camper":str.upper(input("Ingrese su nombre: ")),
        "apell_camper":str.upper(input("Ingrese su apellido: ")),
        "Dirr_camper":str.upper(input("Ingrese su direccion: ")),
        "Estado":0,
        "cc_acudi":int(input("Ingrse numnero de identifiacion del acudiente: ")),
        "nom_acudiente":str.upper(input("Ingrse nombre completo de su acudiente: ")),
        "cc_trainer":0
    }
    return data