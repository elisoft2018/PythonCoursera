"""i = 0
while i < 5:
    print('Hola Mundo')
    i = i + 1

a = 2
b = 1
c = a / b

#a + spam * 1

#d = '2' + 2

while True:
    try:
        x = int(input('Por favor ingrese un número: '))
        break
    except ValueError:
        print('Oops, el valor es valido....Intenta nuevamente')

def esto_falla():
    x = 1 / 0
try:
    esto_falla()
except ZeroDivisionError as err:
    print('Manejando error en tiempo de ejecución',err)

import sys


def dividir(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("¡división por cero!")
    else:
        print("el resultado es", result)
    finally:
        print("ejecutando la clausula finally", '\n')


dividir(2, 0)


class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print('D')
    except C:
        print('C')
    except B:
        print('B')
print('\n')

try:
    f = open('miarchivo.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print('Error OS: {0}'.format(err))
except ValueError:
    print('no pude convertir el dato a un entero')
except:
    print('error inesperado', sys.exc_info()[0])
    raise
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('no pude abrir', arg)
    else:
        print(arg, ' tiene', len(f.readlines()), ' lineas')
        f.close()

print('\n')

try:
    raise Exception('Carne', 'Huevos')
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)

    x, y = inst
    print('x = ', x)
    print('y = ', y)


def esto_falla():
    z = 1 / 0


try:
    esto_falla()
except ZeroDivisionError as err:
    print('Manejando error en tiempo de ejecución:', err)



t = 1 / 0
try:
    t = 1 / 0
except ZeroDivisionError:
    print("División por cero")

import math


def find(elemento, lista):
   Devuelve el indice donde se encuentra el @elemento en la @lista.
         Si no lo encuentra devuelve -1.

    index = 0
    while True:
        try:
            if lista[index] == elemento:
                return index
        except IndexError:
            return -1
        index += 1


# ejemplos de find
print(find(4, [2, 3, 4, 5]))
print(find(1, [2, 3, 4, 5]))


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('División por Cero')
    else:
        print('El resultado es ', result)
    finally:
        print('Ejecutando la clausula Finally')


print(divide(0, 5))
print(divide(10, 5))
print(divide(1, 0))

print('\n')


class NegativeNumber(Exception):
    print("Excepción de Tipo de Numero Negativo")
    pass


def raiz(number):
    if number < 0:
        raise NegativeNumber('Numero negativo')
    return math.sqrt(number)


print(raiz(9))
print(raiz(-4))
"""
