import random

Game = input("Lanzar 2 dados: s / n ")

D1 = random.randint(1, 6)
D2 = random.randint(1, 6)
d3 = D1 + D2


while Game == 's':

    s = "SI" or "Si" or "si" or "S"
            
    print("el primer dado es:")
    print(D1) 
    print("el segundo dado es:")
    print(D2)
    print("La suma de los dados es:")
    print(d3)

    Game = input("Lanzar 2 dados: Si o No ")
  
while Game == 'n':

    print("vamos es solo un juego") 
    print("adios")
    break