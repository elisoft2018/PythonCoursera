#def function(x):
#    result = 0;
#    if x > 0 and x < 5:
#        result = x ** 2
#    elif x >= 5 and x < 10:
#        pass
#    else:
#        result = (x ** 4) + 1
#    return print(result)
#function(2)
#function(7)
#function(12)

#def es_primo(numero):
#    resultado = True
#    for divisor in range(2,numero):
#        if numero % divisor == 0:
#            resultado = False
#            break
#        print(resultado)
#es_primo(13)
#s = 0
#for n in range(1,10):
#    if n % 11 == 0:
#        break
#    s += n
#else:
#    s += 10
#
#print(s)

def prueba():
    s = 0
    for n in range(1, 10):

        if n % 2 != 0:
           continue;
        s += n
        print(s)

    else:
        s += 5
    return print(s)
prueba()



