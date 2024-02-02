def continuar(x):
    print("""
        ¿Quieres continuar?
               1=Si
               2=No""")
    opc=int(input(""))
    while True:
        match(opc):
            case(1):
                break
            case(2):
                x=False
                break
            case(_):
                pass
    return x