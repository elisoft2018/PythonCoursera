def firts_10():
    """Genera los primeros diez números"""
    for x in range(100):
        yield x


gen_firts_10 = firts_10()
print(gen_firts_10)
print("Generar numeros")
for x in gen_firts_10:
    print(x)


def gen_prime_numbers(quoted=1):
    count = 1
    prime_list = []
    """Ciclo infinito para calcular numeros primos"""
    while quoted > count:
        is_prime = True
        count += 1
        if len(prime_list) > 0:
            for prime in prime_list:
                if count % prime == 0:
                    is_prime = False
                    break
        if is_prime:
            prime_list.append(count)
            yield count


firts_prime_100 = gen_prime_numbers(100)

print("Numeros primos")
for prime in firts_prime_100:
    print(prime)
