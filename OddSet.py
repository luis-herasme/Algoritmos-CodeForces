import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

t = int(input())

for _ in range(t):
    input() #n
    two_n = input_list_numbers()
    
    odds = 0
    evens = 0

    for ni in two_n:
        if ni % 2:
            odds += 1
        else:
            evens += 1
    if odds == evens:
        print("Yes")
    else:
        print("No")
    