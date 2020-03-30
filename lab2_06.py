def fiboncciGenerator(n):
    numberslist = list(range(0, n))
    for (i, number) in enumerate(numberslist):
        if number > 1:
            number = numberslist[i - 1] + numberslist[i - 2]
            numberslist[i] = number
        yield number


print('Set Fibonacci length:')
obj = fiboncciGenerator(int(input()))
seq = list(obj)
print(seq)
