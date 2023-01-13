import time


def time_meter(f):
    def wrap(*args, **kwargs):
        ti = int(time.time() * 1000)
        result = f(*args, **kwargs)
        tf = time.time()
        endtime = ti - tf
        print("La funcion ", f.__name__, "Tardó", endtime, "segundos")
        return result

    return wrap


""" @time_meter
def suma(a, b):
    return a + b
"""


def logger(debug=False):
    def _logger(func):
        def inner(*args, **kwargs):
            if debug:
                print('Debug Mode')
                for i, arg in enumerate(args):
                    print("arg %d:%s" % (i, arg))
                return func(*args, **kwargs)

        return inner

    return _logger


@time_meter
@logger(True)
# @logger(False)
def suma(a, b):
    return a + b


resultado = suma(34, 67)
print(resultado)
