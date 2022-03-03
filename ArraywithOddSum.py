
import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

t = int(input())

for i in range(t):
    input() # n
    a = input_list_numbers()
    if sum(a) % 2:
        print("YES")
    else:
        a_has_even = 0
        a_has_odd = 0
        for ai in a:
            if ai % 2:
                a_has_odd = 1
            else:
                a_has_even = 1
            if a_has_even and a_has_odd:
                break
        if a_has_even and a_has_odd:
            print("YES")
        else:
            print("NO")

