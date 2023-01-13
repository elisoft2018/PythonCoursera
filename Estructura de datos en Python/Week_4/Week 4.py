# Tuplas
import singleton as singleton

t = 1234, 543223, 'Hola'
print(t[0])
print(t)

u = t, (1, 2, 3, 4, 5)
print(u)
print(u[1])

# Las tuplas son inmutables

v = ([1, 2, 3, 4, 5], [6, 7, 8])
print(v[0])

# Tuplas Vacias

vacia = ()
singleton = '!Hola¡'
print(len(vacia))
print(len(singleton))
print(singleton)

tp = 'John', 9876, 12245
print(tp)
