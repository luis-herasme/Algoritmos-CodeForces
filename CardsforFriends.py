import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))


t = int(input())

for i in range(t):
    [w, h, n] = input_list_numbers()

    pieces = 1

    while True:

        if pieces >= n:
            print("YES")
            break

        if w % 2 == 0:
            w = w / 2
            pieces = 2 * pieces

        elif h % 2 == 0:
            h = h / 2
            pieces = 2 * pieces

        else:
            print("NO")
            break
