def smart_division(div_func):
    def div(a, b):
        if b == 0:
            print('No se puede dividir por cero')
            return
        return div_func(a, b)

    return div


def log(f):
    def wrap(*args, **kwargs):
        print('Ejecutando la función', f.__name__,
              'con los argumentos', ','.join([str(arg) for arg in args]))
        return f(*args, **kwargs)

    return wrap


@log
@smart_division
def division(a, b):
    return a / b


print(division(2, 3))


@log
def suma(a, b):
    return a + b


print(suma(34, 789))
