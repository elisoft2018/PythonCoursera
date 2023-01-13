# Dictionary
import math

tel = {'John': 3203454612, 'Andrea': 3209434593}
print(tel)
tel['Father'] = 3244356567
print(tel)
print(tel['Andrea'])
print(list(tel.keys()))
print(sorted(tel.keys()))
print('Father' in tel)
print('Alex' in tel)
print('Father' not in tel)
print('Alex' not in tel)
del tel['Father']
print(tel)

# dic()
phone_contacts = [('John', 3243245545), ('Mother', 3245564656), ('Wife', 32932434567)]
print(phone_contacts)
print(dict(phone_contacts))

pown = {x: x ** 2 for x in (2, 4, 6)}
print(pown)

contact = dict(shape=121344, guido=456456, jack=35454)
print(contact)

# Technicals de iteration

caballeros = {'gallahad': 'el puro', 'robin': 'el valiente'}
for k, v in caballeros.items():
    print(k, v)

for i, v in enumerate(['a', 'e', 'i', 'o', 'u']):
    print('rewrewrrewrw',i, v)

questions = ['nombre', 'objetivo', 'color favorito']
answers = ['lancelot', 'el santo grial', 'azul']

for p, r in zip(questions, answers):
    print('Cual es tu {0}?  {1}'.format(p, r))

for i in reversed(range(1, 10, 2)):
    print(i)

canasta = ['manzana', 'naranja', 'manzana', 'pera', 'naranja', 'banana']
for f in sorted(set(canasta)):
    print(f)

dates = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
print(dates)
filter_dates = []
for x in dates:
    if not math.isnan(x):
        filter_dates.append(x)
print(filter_dates)

price = {'Apple': 3, 'Banana': 2.5, 'Kiwi': 4}
print(price)
print(price['Banana'])
print(price['Kiwi'])
price['lemon'] = 5.5
print(price)
price['Banana'] = 3.5
print(price)

prices = dict(tomate=20, rice=30, pasta=40)
print(prices)
prices['potatoe'] = 50
print(prices)

del price['Apple']
print(price)

del prices['tomate']
print(prices)

x = 'Banana' in prices
y = 'rice' in price
z = 'Kiwi' in price
w = 'pasta' in prices
print(x)
print(y)
print(z)
print(w)



