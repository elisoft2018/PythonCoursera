def gen_10():
    for n in range(10):
        yield n


gen_numbers = gen_10()
print(next(gen_numbers))
print(next(gen_numbers))
print(next(gen_numbers))
print(next(gen_numbers))
print(next(gen_numbers))
print(next(gen_numbers))
print(next(gen_numbers))
print(next(gen_numbers))
print(next(gen_numbers))
print(next(gen_numbers))

print('Naturales')


def naturales(n):
    n = 1
    while True:
        yield n
        n = n + 1


naturales = naturales(10)
print(next(naturales))
print(next(naturales))
print(next(naturales))
print(next(naturales))
print(next(naturales))
print(next(naturales))
print(next(naturales))
print(next(naturales))
print(next(naturales))

pares = [x for x in range(10) if x % 2 == 0]
print(pares)
pares_1 = (p for p in range(10) if p % 2 == 0)
print(pares_1)
