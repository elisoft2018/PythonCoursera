import string

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.punctuation)
print(string.printable)
print(string.whitespace)


s = 'Python'

# Acceso a los argumentos por posición
print('Hola, {}'.format(s))
print('{}+{}={}'.format(2,5,7))
print('{1}+{2}={0}'.format(7,5,2))

# Acceso a los argumentos por nombre
print('Mira {name}'.format(name=s))
print('{0}+{1}={result}'.format(5,2,result= 7))

# Acceso a los elementos del argumento
tupla = (4,3)
print('X:{0[0]}; Y:{0[1]}'.format(tupla))

# Aplicando formato a los elementos
print('{0:f}+{1:f}={resul:f}'.format(2,5,resul = 7))
print('{0:.3f}+{1:.3f}={resul:.3f}'.format(2,5,resul = 7))
print('{:d}'.format(25))
print('{:.0f}'.format(25.50))

# Alineación del texto reemplazado
print('Hola {name:16}'.format(name = s))
print('Hola {name:<16}'.format(name = s))
print('Hola {name:>16}'.format(name = s))
print('Hola {name:^16}'.format(name = s))
print('Hola {name:*^16s}'.format(name = s))
print(' {name:*^10  s}'.format(name = s))


