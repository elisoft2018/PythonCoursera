import csv

"""
print('OBJETO READER')
with open('Libreria.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print('\n')
with open('Libreria.csv', newline='') as f:
    reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
    for row in reader:
        print(row)

print('\n')

with open('Libreria.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        print(', '.join(row))

print('\n')

csv.register_dialect('unixpwd', delimiter=':', quoting=csv.QUOTE_NONE)
with open('Libreria.csv', newline='') as f:
    reader = csv.reader(f, 'unixpwd')
    for row in reader:
        print(row)

print('\nOBJETO DICTREADER')

with open('Libreria.csv', newline='') as csvfiles:
    reader = csv.DictReader(csvfiles)
    for row in reader:
        print(row['Nombre'], row['Apellido'])
print('\n')


someIterable = [['1', '2', '3'], ['5', '6', '7']]
with open('some.csv', 'w', newline='') as fl:
    writer = csv.writer(fl)
    writer.writerows(someIterable)

with open('some.csv', 'r', newline='') as fle:
    reader = csv.reader(fle)
    for row in reader:
        print(row)

print('\n')

print('Escritura de archivos CSV, objeto WRITER')

with open('Libreria.csv', 'a', newline='') as fileCsv:
    writer = csv.writer(fileCsv, delimiter=',', quotechar='|',
                        quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Pedro', 'Perez'])
    writer.writerow(['Luis', 'Alba'])

with open('Libreria.csv', 'r', newline='') as p:
    reader = csv.reader(p, delimiter=',', quoting=csv.QUOTE_NONE)
    for row in reader:
        print(row)


print('Escritura de archivos CSV, objeto DIC_WRITER')

with open('Libreria.csv', 'a', newline='') as dw:
    fieldnames = ['Nombre', 'Apellido']
    writer = csv.DictWriter(dw, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Nombre': 'Pablo', 'Apellido': 'Alba'})
    writer.writerow({'Nombre': 'Jose', 'Apellido': 'Rodriguez'})

with open('Libreria.csv', newline='') as dwFiles:
    reader = csv.DictReader(dwFiles)
    for row in reader:
        print(row['Nombre'], row['Apellido'])
"""

import json

# serializer un objeto

sre = json.dumps([1, 2, 3])
print(sre)

# Deserializer un objeto

sre2 = json.loads('[1, 2, 3, 4]')
print(sre2)

# Escribir como Json directamente en un archivo
with open('sample.json', 'w') as a_file:
    json.dump([1, 2, 3, 4, 5], a_file)

# Leer un Json directamente desde un archivo
with open('sample.json', 'r') as a_OpenFile:
    a_list = json.load(a_OpenFile)
    print(a_list)

# Leer archivo de CSV
with open('Libreria.csv', 'r') as fileRead:
    reader = csv.reader(fileRead)
    for row in reader:
        print(', '.join(row))

# Escribir en un archivo excel
with open('Libreria.csv', 'a', newline='') as writerFile:
    writer = csv.writer(writerFile)
    writer.writerow(['Felix', 'Machado'])

with open('task.txt', 'w', newline='') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONE, quotechar='|', doublequote=False)
    writer.writerow(['Hola Mundo'])

