import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

[n, k, l, c, d, p, nl, np] = input_list_numbers()


print(min((k * l) // nl, c * d, p // np) // n)