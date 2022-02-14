import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

t = int(input())
s_list = [None] * t

for i in range(t):
    input() # n
    s_list[i] = input_list_numbers()

for s in s_list:
    s.sort()
    derivative = [None] * ( len(s) - 1 )
    for i in range(len(s) - 1):
        derivative[i] = abs(s[i + 1] - s[i])
    print(min(derivative))
