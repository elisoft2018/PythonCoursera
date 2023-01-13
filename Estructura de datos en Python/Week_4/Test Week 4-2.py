precios = {'manzana': 3.5, 'banana': 4.5, 'kiwi': 6.0, 'pera': 3.75, 'ciruela': 2.45, 'durazno': 4.55, 'melon': 7.35,
           'sandia': 9.70, 'anana': 11.25}

quantity = {'manzana': 2, 'banana': 2.5, 'kiwi': 1, 'pera': 3, 'ciruela': 1, 'durazno': 2,
            'melon': 5, 'sandia': 10, 'anana': 3}
total_amount = 0

for fruit_quoted, quoted in quantity.items():
    for fruit, price in precios.items():
        if fruit_quoted == fruit:
            total = quoted * price
            total_amount = total_amount + total
            print(fruit, '|', price, '$', '|', quoted, 'Kg', '|', total, '$')
print('El precio total de la compra es ', total_amount)


d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
d.update((('a', 1), ('b', 2)))
print(d)
