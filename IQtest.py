import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

input()
numbers = input_list_numbers()

# Revisar si es uno de los primeros 3
n1 = numbers[0] % 2
n2 = numbers[1] % 2
n3 = numbers[2] % 2

is_in_the_start = 0
if n1 + n2 + n2 == 0:
    what_is_normal = 0
elif n1 + n2 + n2 == 3:
    what_is_normal = 1
else:
    is_in_the_start = 1
    if n1 == n2:
        print(3)
    elif n1 == n3:
        print(2)
    elif n2 == n3:
        print(1)

if not is_in_the_start:
    for (idx, n) in enumerate(numbers):
        if (n%2) != what_is_normal:
            print(idx + 1)
            break
