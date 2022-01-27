import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

n = int(input())

pi_list = input_list_numbers()
result = [None] * n

for idx, value in enumerate(pi_list):
    result[value - 1] = idx + 1

print(' '.join(map(str, result)))

