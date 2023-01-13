"""import math

s = "Hola Mundo"
print(str(s))
print(repr(s))
print(str(1 / 7))

print('\n')

x = 10 * 3.25
y = 200 * 200
s = 'El valor de x es ' + repr(x) + ', y es ' + repr(y) + '....'
print(s)

print('\n')

hola = 'hola mundo\n'
holas = repr(hola)
print(holas)

print('\n')

print(repr((x, y, ('carne', 'huevos'))))

print('\n')

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end='')
    print(repr(x * x * x).rjust(4))

print('\n')

for x in range(1, 11):
    print('{0:2d},{1:3d},{2:4d}'.format(x, x * x, x * x * x))

print('\n')

print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.1443445455'.zfill(5))

print('\n')

print('Los {}  somos quienes decimos {}'.format('Caballeros', 'No!'))
print('{0} y {1}'.format('Carne', 'Huevo'))
print('la {comida} es {adjetivo}'.format(comida='Carne', adjetivo='espantosa'))
print('El {animal} es un {0} del {1}'.format('hervivoro', 'campo', animal='Caballo'))

print('\n')

contents = 'anguilas'
print('mi aerodeslizador esta lleno {}'.format(contents))
print('my hovercraft is full {!r}.'.format(contents))

print('\n')

print('el valor de PI es aproximadamente {0:.3f}'.format(math.pi))

print('\n')

tabla = {'John': 4350, 'Eliseo': 3435, 'Andres': 5456}
for nombre, telefono in tabla.items():
    print('{0:10} ===> {1:10d}'.format(nombre, telefono))
print('John: {0[John]:d};Eliseo: {0[Eliseo]:d};Andres: {0[Andres]:d}'.format(tabla))
print('John:{John:d};Eliseo:{Eliseo:d};Andres:{Andres:d}'.format(**tabla))
print('\n')
f = open('pruebaLecturaArchivo.txt', 'w')
f.write('Cebolla')
f.close()
f = open('pruebaLecturaArchivo.txt')
# print("Datos del archivo con read\n ", f.read())
# print("Datos del archivo con readline\n", f.readline())
# for linea in f:
#    print("Leer datos del archivo con ciclo", linea, end='')
print(f.readlines())
# print(list(f))

print('\n')
with open('miarchivo.txt') as fl:
    reading_dates = fl.read()
fl.close()
# fl.read()
print(fl)
print('\n')

fz = open('pruebaLecturaArchivo.txt', 'w')
valor = 'la respuesta'
s = str(valor)
fz.write(s)
fz.close()
fz = open('pruebaLecturaArchivo.txt')
print(fz.read())
print(fz.tell())
fz.close()
fz = open('pruebaLecturaArchivo.txt', 'rb+')
fz.write(b'1234567890abcdef')
print(fz.seek(5))
print(fz.read(1))
print(fz.seek(-3, 2))
print(fz.read(1))

import json

dictionary ={
  "id": "04",
  "name": "sunil",
  "department": "HR"
}

json_object = json.dumps(dictionary, indent=4)
print(json_object)

with open("sample.json", 'w') as outfile:
    json.dump(dictionary,outfile)


# a_file = open("pruebaLecturaArchivo.txt", 'r')
# print(a_file.read())
# a_file.close()
with open("pruebaLecturaArchivo.txt", 'r') as a_file:
    print(a_file.read())

with open("pruebaLecturaArchivo.txt", 'r') as a_file:
    print(a_file.readline())

with open("pruebaLecturaArchivo.txt", 'r') as a_file:
    print(a_file.readlines())

with open("pruebaLecturaArchivo.txt", 'r') as a_file:
    print(list(a_file))

with open("pruebaLecturaArchivo.txt", 'r') as a_file:
    for line in a_file:
        print(line)


"""

with open("pruebaLecturaArchivo.txt", 'w') as a_file:
    a_file.write('Hola Mundo')

with open("pruebaLecturaArchivo.txt", 'w') as a_file:
    a_file.writelines(['linea 1\n', 'linea 2\n', 'linea 3\n', 'linea 4\n', 'linea 5'])

with open("pruebaLecturaArchivo.txt", 'a') as a_file:
    a_file.write('\nHola Mundo desde Python')

