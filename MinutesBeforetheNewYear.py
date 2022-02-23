import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

t = int(input())

for i in range(t):
    [h, m] = input_list_numbers()
    print((23 - h) * 60 + 60 - m)
