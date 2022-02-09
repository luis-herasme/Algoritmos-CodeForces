import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

t = int(input())
a_list = [None] * t

for i in range(t):
    input() # N
    a_list[i] = input_list_numbers()


for j in range(t):
    a = a_list[j]
    bad_elements_even = 0
    bad_elements_odd  = 0

    for i in range(len(a)):
        if i % 2 != a[i] % 2:
            if a[i] % 2:
                bad_elements_odd = bad_elements_odd + 1
            else:
                bad_elements_even = bad_elements_even + 1
    if bad_elements_odd == bad_elements_even:
        print(bad_elements_even)
    else:
        print(-1)
    



