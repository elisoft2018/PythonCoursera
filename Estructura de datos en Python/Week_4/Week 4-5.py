price = {'Apple': 3, 'Banana': 2.5, 'Kiwi': 4, 'orange': 7, 'grapes': 4.5, 'strawberry': 10}
# Vistas de los diccionarios
key_code = price.keys()
print(key_code)
values = price.values()
print(values)
items = price.items()
print(items)

price['melon'] = 1.5

key_code = price.keys()
print(key_code)
values = price.values()
print(values)
items = price.items()
print(items)

# Iteración de diccionarios
for fruta, precio in price.items():
    print('Fruta: ', fruta, '$: ', precio)
