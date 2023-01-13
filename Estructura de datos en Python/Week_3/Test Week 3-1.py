numbers = [x for x in range(1, 101) if x % 2 == 0]
print(numbers)
# numbers_one = [x for x in range(10) if x % 2 == 1]
# numbers_one = [x for x in range(10) if x % 2 != 0]
# numbers_one = [x for x in range(10) if x % 2 != 1]
# numbers_one = [x*2 + 1 for x in range(5)]
# numbers_one = [x*y for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
# numbers_one = list(map(lambda x: x**2, range(10)))
# numbers_one = list(filter(lambda x: x**2, range(10)))
numbers_one = list(map(lambda x: x**2 > 0, range(10)))

print(numbers_one)
