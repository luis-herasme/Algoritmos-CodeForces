import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))


def opposite(x, size):
    if x <= (size / 2):
        return x + size // 2
    else:
        return x - size // 2

t = int(input())

for i in range(t):
    [a, b, c] = input_list_numbers()
    size = 2 * abs(a - b)
    if a > size or b > size or c > size:
        print(-1)
    else:
        print(opposite(c, size))