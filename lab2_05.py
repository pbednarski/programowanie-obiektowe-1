def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True


numbersList = list(range(100))

primeNumbersFilter = list(filter(lambda x: isPrime(x), numbersList))
print(primeNumbersFilter)
print('-------------------------------------------------------------------------------------------------')

primeNumbersMap = list(map(lambda x: isPrime(x), numbersList))
primeNumbersListMap = []

for i, el in enumerate(primeNumbersMap):
    if primeNumbersMap[i]:
        primeNumbersListMap.append(numbersList[i])

print(primeNumbersListMap)
