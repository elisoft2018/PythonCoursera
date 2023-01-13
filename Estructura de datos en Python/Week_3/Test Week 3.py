a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sublist = [2, 3, 4, 5, 6, 7, 8]
a_list = sublist
print(a_list)
a_list.append(9)
print(a_list)
print(a_list)
a_list.insert(0, 5)
print(a_list)
a_list.remove(5)
a_list.pop()
print(a_list)

# Ordenamiento de elementos de la lista
a_list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Ordena los elementos de la lista in situ
a_list_one.sort()
print(a_list_one)
a_list_one.sort(reverse=True)
print(a_list_one)
a = [(1, 9), (1, 3), (1, 4), (1, 2)]
a.sort(key=lambda x: x[1])
print(a)

# Revierte los elementos de la lista
a_list_two = [3, 1, 2, 9, 5, 4, 7, 8, 6]
a_list_two.reverse()
print(a_list_two)
# ordena los elementos y crea una nueva lista

print(sorted(a_list_two))

print(sorted(a_list_two, reverse=True))

print(sorted(a, key=lambda x: x[1]))

for x in range(10):
    print(x)
