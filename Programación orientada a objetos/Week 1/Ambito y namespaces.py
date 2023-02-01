def pruebas_ambitos():
    def hacer_local():
        algo = "Algo local"

    def hacer_nonlocal():
        nonlocal algo
        algo = "Algo no local"

    def hacer_global():
        global algo
        algo = "Algo global"

    algo = "Algo de prueba"
    hacer_local()
    print("Luego de la asignación local: ", algo)
    hacer_nonlocal()
    print("Luego de la asignación no local: ", algo)
    hacer_global()
    print("Luego de la asignación global: ", algo)


pruebas_ambitos()
print("In global scope: ", algo)
