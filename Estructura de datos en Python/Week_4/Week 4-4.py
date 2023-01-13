price = {'Apple': 3, 'Banana': 2.5, 'Kiwi': 4, 'orange': 7, 'grapes': 4.5, 'strawberry': 10}
print(price)
# Cantidad de elementos del diccionario
print('Numeros de elementos', len(price))

# Obtener el valor para la clave indicada, se puede indicar un default si no existe

print('Precio ', price.get('Apple'))
print('Precio ', price.get('orange'))
print('Precio ', price.get('melon'))
print('Precio ', price.get('melon', 0.0))

# Si existe devuelve el valor, si no lo crea con el valor por default o si no se indica el default con none
print(price.setdefault('Banana'))
price.setdefault('Sandia', 9.8)
print(price)

# Actualización de un diccionario

price.update({'Apple': 5.6, 'Durazno': 11})
print(price)
price.update([('Durazno', 4)])
print(price)

# Me devuelve una vista con las claves del diccionario

print(price.keys())

# Me devuelve una vista con los valores del diccionario

print(price.values())

# Me devuelve una vista con los items del diccionario

print(price.items())

# Saca el elemento de la clave indicada, se puede poner un default si no existe
price.pop('Durazno')
print(price)
price.pop('melon', 0.0)
print(price)

# Saca un elemento siguiendo el orden : LIFO

price.popitem()
print(price)

# Copia superficial de los diccionarios
copy_price = price.copy()
print(copy_price)

# Borra los todos elementos del diccionario
price.clear()
print(price)