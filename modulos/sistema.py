def continuar():
    X=True
    print("""
        ¿Quieres continuar?
               1=Si
               2=No""")
    opc=int(input(""))
    while True:
        match(opc):
            case(1):
                x=True
                break
            case(2):
                x=False
                break
            case(_):
                pass
    return x