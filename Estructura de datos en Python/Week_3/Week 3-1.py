frutas = {'manzana', 'pera', 'naranja', 'kiwi', 'uvas', 'naranja', 'pera', 'uvas'}
print(frutas)
print('manzana' in frutas)
print('mandarina' in frutas)
a = set('abracadabra')
b = set('alakazam')
print(a)
print(b)
print(a - b)  # Letras en a pero no en b
print("prueba ", a | b)  # Letras en a o en b o en ambas
print(a & b)  # Letras en a y en b
print(a ^ b)  # Leras en a o b pero no en ambos

# Comprensión de conjuntos
c = {x for x in a if x not in 'abc'}
print(c)
c.add('w')
print(c)
c.remove('r')
print(c)
matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
matriz2 = [
    [13, 14, 15, 16],
    [17, 18, 19, 20],
    [21, 22, 23, 24]
]
print(matriz)
print(matriz2)

# Acceso por indexación
print(matriz[0][1])
print(matriz[1][2])


# Funcion suma de matrices
def suma_matrices(a, b):
    cant_rows = len(a)
    cant_colum = len(a[0])
    c = []
    for row in range(cant_rows):
        fila_suma = []
        for colum in range(cant_colum):
            fila_suma.append(a[row][colum] + b[row][colum])
        c.append(fila_suma)
    return c


print(suma_matrices(matriz, matriz2))

[[1, 2, 3],
 [1, 3, 2],
 [3, 1, 2]]
