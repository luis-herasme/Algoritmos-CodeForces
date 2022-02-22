import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

t = int(input())

def algo(a, b):

    moves = 0

    while True:
        d = a - b
        # print("d: ", d)
        if d == 0:
            return moves

        if d % 2 == 0:
            even = abs(d)
            odd = abs(d) - 1
        else:
            odd = abs(d)
            even = abs(d) + 1

        if d > 0:
            if even == 0:
                even = 2
            # print("even: ", even)
            a -= even
        else:
            if odd == 0:
                odd = 1
            # print("odd: ", odd)
            a += odd

        moves += 1


for i in range(t):
    [a, b] = input_list_numbers()
    print(algo(a, b))