#n = input('Digite un numero ')
#n= int(n)
#def fibonacci(n):
#    """Escribe la serie de Fibonacci hasta n."""
#    a, b = 0, 1
#    while a < n:
#        print(a, end=' ')
#        a, b = b, a+b
#        print()
#f=fibonacci
#f(n)
#print(fibonacci(0))

#def fib(n):
#    result = []
#    a , b = 0 , 1
#    while a < n:
#        result.append(a)
#        a , b = b , a + b
#        #print(result)
#    print(result)
#fib(n)

#def pedir_confirmacion(prompt,reintetos=4,recordatorio='Por favor, intente nuevamente!'):
#    while True:
#        ok = input(prompt)
#        if ok in ('s','S','si','Si','SI'):
#            return True
#        if ok in ('n','N','no','No','NO'):
#            return False
#        reintetos -=1
#        print(reintetos)
#        if reintetos <= 0:
#            raise ValueError('Respuesta de usuario invalida')
#        print(recordatorio)
#pedir_confirmacion('¿Sobreescribir archivo?', 4, 'Vamos, solo si o no!')

#i = 5
#def f(arg = i):
#    print(arg)
#i = 6
#f()
#def  f(a , L = []):
#    L.append(a)
#    return L
#print(f(5))
#print(f(4))
#print(f(3))
#print(f(2))
#print(f(1))

#def f1(a , L=None):
#    if L is None:
#        L=[]
#        L.append(a)
#    return L
#print(f1(3))
#print(f1(2))
#print(f1(1))

#def loro(tension, estado='muerto', accion='explotar', tipo='Azul Nordico'):
# print("-- Este loro no va a", accion, end=' ')
# print("si le aplicás", tension, "voltios.")
# print("-- Gran plumaje tiene el", tipo)
# print("-- Está", estado, "!")
#loro(4)

#def funcion(a):
#    pass
#funcion(0 , a = 0)

#def ventadequeso(tipo, *argumentos, **palabrasclaves):
# print("-- ¿Tiene", tipo, "?")
# print("-- Lo siento, nos quedamos sin", tipo)
# for arg in argumentos:
#    print(arg)
# print("-" * 40)
# for c in palabrasclaves:
#    print(c, ":", palabrasclaves[c])
#
#ventadequeso("Limburger", "Es muy liquido, sr.",
# "Realmente es muy muy liquido, sr.",
# cliente="Juan Garau",
# vendedor="Miguel Paez",
# puesto="Venta de Queso Argentino")

#def concatenar(*args,sep='/'):
#    return sep.join(args)
#print(concatenar('lunes','martes','miercoles'))
#print(concatenar('lunes','martes','miercoles',sep='.'))

#secuencia = range(3,6)
#print(list(secuencia))
#
#args = [3,6]
#secueciaDesempaquetada = range(*args)
#print(list(secueciaDesempaquetada))

#def loro(tension, estado='rostizado', accion='explotar'):
#     print("-- Este loro no va a", accion, end=' ')
#     print("si le aplicás", tension, "voltios.", end=' ')
#     print("Está", estado, "!")
#loro(400)

#d = {"tension": "cinco mil", "estado": "demacrado",
#     "accion": "VOLAR"}
#loro(**d)

#n = input('numero inicial ')
#n = int(n)
#def hacerIncrementador(n):
#    return lambda x:x + n 
#
#f = hacerIncrementador(42)
#print(f(0))
#print(f(1))

#def mi_funcion():
#     """No hace mas que documentar la funcion.
#
#     No, de verdad. No hace nada.
#     """
#     pass
#
#print(mi_funcion.__doc__)

#def f(jamon: str, huevos: str = 'huevos') -> str:
#    print("Anotaciones:", f.__annotations__)
#    print("Argumentos:", jamon,' y ', huevos)
#    return jamon + ' y ' + huevos
#f('Carne')

#def cero():
#    return 0
#print (cero() + 1)
#
#def suma_uno(un_numero):
#    return un_numero + 1
#print(suma_uno(5))
#print(suma_uno(cero()))

#def suma (a, b):
#    resultado = a + b
#    return resultado
#print(suma(50,20))

#def maximo_2(a, b):
#    "Devuelve el numero máximo entre a y b"
#    maximo = a
#    if b > a:
#        maximo = b
#    else:
#        maximo = a
#    return maximo
#print(maximo_2(2,5))

#def maximo_3(a, b, c):
#    "Devuelve el numero máximo entre a, b y c"
#    return maximo_2(a, maximo_2(b, c))
#print(maximo_3(6, 1, 5))

#def peso(masa, gravedad = 9.8):
#    "Formula del peso"
#    return masa * gravedad
##Parámetros opcionales
#print("Peso en la tierra: ",peso(10))
#print("Peso en la luna: ", peso(10, 1.63))
##Parámetros con palabras claves(o argumentos nombrados)
#print("Peso en la luna: ", peso(10, gravedad = 1.63))
#print("Peso en la luna: ", peso(masa = 10, gravedad = 1.63))
#print("Peso en la luna: ", peso(gravedad = 1.63, masa = 10))

##Lista de parámetros
#def suma_numeros(*args):
#    "Suma los numeros pasados por parámetros"
#    return sum(args)
#print("4 + 5 + 6 = ",suma_numeros(*[4,5,6]))
#print("4 + 5 + 6 = ",suma_numeros(4,5,6))

##Diccionario de parámetros
#def imprimir_ticket(*args, **kwargs):
#    "Imprime el ticket de una compra"
#    print("Detalle del Ticket")
#    for item , precio in kwargs.items():
#        print(item,":",precio)

#Expresiones lambda
#import time

#f = lambda x:x + 1
#print("Tipo de la variable f es :",type(f))
#print("f(3) = ",f(3))
#
#def function_time(f,*args):
#    start_time = time.time()
#    result = f(*args)
#    end_time = time.time()
#    execution_time = end_time - start_time
#    print("Tiempo de ejecución: ",execution_time, "milisegundos")
#    return result
#print("f(5) = ", function_time(f,10))

#n = input("Digite el numero de la serie: ")
#n = int(n)
#def fib (n):
#    if n < 2:
#        return n 
#    else:
#        return fib(n-1) + fib(n-2)
#r = fib(n)
#print(r)

#for x in range(10,0,-1):
#    print(x)
#secuencia = range(2,13,2)
#print(list(secuencia))

#import pdb
#pdb.set_trace()



def a_function(a_number):
    """
    Si la función recibe un numero a_number y hace:
    Si el numero es par:
        Si es multiplo de 10
            Devolver el resultado de dividir el numero por 2.
        Si es multiplo de 8
            Devolver el resultado de dividir el numero por 2.
        Sino 
            Restarle 1   
    Si el numero es impar:
        Si es multiplo de 3:
             Devolver el resultado de multiplicar el numero por 11.      
        Si es multiplo de 7:
            Devolver el resultado de multiplicar el numero por 23.
        Sino:
            Sumarle 1
    """
    #import pdb
    #pdb.set_trace()
    result = None
    if a_number % 2 == 0:
        if a_number % 10 == 0:
            result = a_number / 2
        elif a_number % 8 == 0:
            result = a_number / 2
        else:
            result = a_number - 1
    else:
        if a_number % 3 == 0:
            result = a_number * 11
        elif a_number % 7 == 0:
            result = a_number * 23
        else:
            result = a_number + 1
    return result

result_1 = a_function(20)
print(result_1)



