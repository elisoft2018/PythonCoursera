import math

factorial_10 = str(math.factorial(10))
factorial_result = open('resultadoFactorial.txt', 'w')
factorial_result.write(factorial_10)
factorial_result.close()

f = open('pruebas.txt')

