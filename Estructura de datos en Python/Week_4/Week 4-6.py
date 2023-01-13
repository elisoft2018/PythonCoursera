import datetime

a_dict = dict()

# Key_code
a_dict['Clave'] = 1
print(a_dict)
a_dict[1] = 1
print(a_dict)
a_dict[1.5] = 1
print(a_dict)
a_dict[(1, 2)] = 1
print(a_dict)
a_dict[datetime.date.today()] = 1
print(a_dict)

# Una lista es un contenedor no inmutable,no puede ser hasheable

# a_dict[[1, 2]] = 1
# print(a_dict)

# Lo mismo con los conjuntos

# a_dict[{'a'}] = 1
# print(a_dict)

# Lo mismo con los diccionarios

a_dict[{'a', 1}] = 1
print(a_dict)
