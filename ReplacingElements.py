import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

t = int(input())

for _ in range(t):
    [n, d] = input_list_numbers()
    a = input_list_numbers()
    a.sort()

    all_elements_less_than_d = True

    for ai in a:
        if ai > d:
            all_elements_less_than_d = False
            break

    if a[0] + a[1] <= d or all_elements_less_than_d:
        print("YES")
    else:
        print("NO")
