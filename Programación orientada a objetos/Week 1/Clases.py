"""Creación de Clases en Python"""


class MiClase:
    """Simple clase de ejemplo"""
    i = 12345

    def f(self):
        return "Hola Mundo"


"""Instaciación de Clases en Python"""
x = MiClase()
print(x.f())

"""Objetos de Método
x.f()
xf = x.f
while True:
    print(xf())
"""


class complejo:
    def __init__(self, partereal, parteimaginaria):
        self.r = partereal
        self.i = parteimaginaria


x = complejo(3.0, -4.5)
print("Parte real ", x.r, "Parte Imaginaria", x.i)

"""Objetos de Instancia"""

x.contador = 1
while x.contador <= 10:
    x.contador = x.contador * 2

print("El valor es", x.contador)
del x.contador


class Perro:
    tipo = "canino"  # Variable de clase compartida por todas las instancias

    # trucos = []  # Uso incorrecto de una variable de clase

    def __init__(self, nombre):
        self.nombre = nombre  # Variable de instancia única para la instancia
        self.trucos = []  # crea una nueva lista vacía para cada perro

    def agregar_truco(self, truco):
        self.trucos.append(truco)


d = Perro("Simón")
e = Perro("Tobby")
d.agregar_truco("Girar")
e.agregar_truco("Hacerse el muerto")
"""La variable truco es compartida por toda la clase
print(d.nombre, "Es", d.tipo, "Truco", d.trucos)  # Tipo compartido por todos los perros, Nombre es único
print(e.nombre, "Es", e.tipo, "Truco", e.trucos)  # Tipo compartido por todos los perros, Nombre es único
"""
print(d.nombre, "Es", d.tipo, "ETruco", d.trucos)
print(e.nombre, "Es", e.tipo, "Truco", e.trucos)
