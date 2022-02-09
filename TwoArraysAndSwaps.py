
import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

t = int(input())
nks_list = [None] * t
as_list = [None] * t
bs_list = [None] * t

for i in range(t):
    nks_list[i] = input_list_numbers()
    as_list[i] = input_list_numbers()
    bs_list[i] = input_list_numbers()

for i in range(t):
    [n, k] = nks_list[i]
    a = as_list[i]
    b = bs_list[i]

    a.sort()
    b.sort()

    for j in range(1, k + 1):
        if b[-j] > a[j - 1]:
            a[j - 1] = b[-j]

    print(sum(a))


