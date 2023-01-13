from random import randint


def dados_lanzar_dados():

    lanzarNuevamente = True
    while lanzarNuevamente:
        dado_1 = randint(1,6)
        dado_2 = randint(1,6)

        suma = dado_1 + dado_2

        print("Dado 1 = ",dado_1,"\nDado 2 = ",dado_2)
        print("La suma de los numeros de los dados es = ",suma)

        lanzarNuevamente =  ("s" or "si") in input("Desea volver a lanzar los dados,digita SI para continuar o NO para terminar ").lower()

dados_lanzar_dados()


