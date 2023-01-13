"""String's en Python"""

a_string = "Hola mundo!"
a_string1 = 'Hola mundo!'
a_string2 = """Hola mundo
 esdeefrfrfrefr!"""
a_string3 = '''Hola mundo 
dededfrefrfere!'''
print("texto como comillas dobles")
print(a_string)
print(a_string[0])
print(a_string[-1])
print(a_string[:4])
print(a_string)
print(a_string2)
print(a_string3)
new_string = a_string+'?'
print(new_string)
new_string = a_string[:6]+'o'+a_string[7:]
print(new_string)
print('Hola \r mundo')

name = "Agustín"
print("Hola %s" % name) # Resultado: Hola Agustín
print("El número es %d" % 5 )# Resultado: El número es 5
print("El número es %02d" % 5) # Resultado: El número es 005
print("El decimal es %f" % 6.5 )# Resultado: El número es 6.500000
print("El decimal es %.2f" % 6.5 )# Resultado: El número es 6.50
print("Hola %(name)s" % {'name': name}) # Resultado: Hola Agustín

print("HOLA {}".format(name))
print("la suma de 2+1 {0}".format(2+1))
print(' '.join(["HoLA", name]))
print(','.join(["1","2","2","4"]))

a_name = "Otoño"
coding_string = a_name.encode('utf-8')
print(coding_string)
decoding_string = coding_string.decode('utf-8')
print(decoding_string)

