import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

t = int(input())
tests = [None] * t

for i in range(t):
    tests[i] = input_list_numbers()

for test in tests:
    small_side = min(test)
    big_side = max(test)

    if 2 * small_side >= big_side:
        print((2*small_side)**2)
    else:
        print(big_side**2)