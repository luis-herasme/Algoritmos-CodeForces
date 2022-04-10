from math import ceil

N1 = int(input())
N2 = int(input())

def getHalfDigits(n, new_digits):
    a = 0
    b = 0
    digits = len(str(n))

    for i in range(1, new_digits + 1):
        b += n % (10 ** i) - n % (10 ** (i - 1))
    for i in range(new_digits + 1, digits + 1):
        a += n % (10 ** i) - n % (10 ** (i - 1))
    a = a // (10 ** (new_digits))

    return [a, b]

def karatsubaMultiplication(x, y, l = 1):
    digits = min(len(str(x)), len(str(y)))

    if digits == 1:
        return x * y
    else:
        new_digits = ceil(digits / 2)
        [a, b] = getHalfDigits(x, new_digits)
        [c, d] = getHalfDigits(y, new_digits)

        r1 = karatsubaMultiplication(a, c, l + 1)
        r2 = karatsubaMultiplication(b, d, l + 1)
        r3 = karatsubaMultiplication(a + b, c + d, l + 1)
        r4 = r3 - r2 - r1
        r5 = r1 * (10 ** (new_digits * 2)) + r2 + r4 * (10 ** (new_digits))

        return int(r5)

algo = karatsubaMultiplication(N1, N2)
real = N2 * N1

print('ALGO: ', algo)
print('REAL: ', real)
print(algo == real)



