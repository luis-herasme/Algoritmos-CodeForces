def narcissistic( value ):
    # Code away
    c = 1
    u = 0
    digits = []
    initial = value

    while u < initial:
        digit = value % 10 ** c
        if c > 1:
            digit = digit // 10 ** (c - 1)
        value -= digit

        digits.append(digit)
        u += 10 ** c
        c += 1

    total = 0
    for digit in digits:
        total += digit ** (c-1)

    return (total == initial)

print(narcissistic(371))
