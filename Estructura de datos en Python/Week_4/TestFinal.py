def num_par(n):
    return (x for x in range(n) if x % 2 == 0)


par = num_par(15)
next(par)
next(par)
print(list(par))

