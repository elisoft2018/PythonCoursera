# Empaquetado de tuplas
a = 30
b = 'T'
c = 'A'

tupla = a, b, c
print(tupla)

# Desempaquetado de tuplas
x, y, z = tupla
print(x)
print(y)
print(z)

# Errores  por distintos tamaños a desempaquetar
x, y = tupla
w, x, y, z = tupla