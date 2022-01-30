from cmath import inf
import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

input()
numbers = input_list_numbers()

max = -inf
min = inf

amazing = 0

for (idx, n) in enumerate(numbers):

    if idx == 0:
        max = n
        min = n

    else:
        if n < min:
            min = n
            amazing = amazing + 1

        if n > max:
            max = n
            amazing = amazing + 1

print(amazing)