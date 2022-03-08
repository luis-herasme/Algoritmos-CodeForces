import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

t = int(input())


    
for _ in range(t):
    input() #n
    a = input_list_numbers()
    
    a_mean = sum(a) / len(a)

    if a_mean == 1:
        print(0)
        continue

    x = len(a) + 1 - sum(a)

    if x < 0:
        s = sum(a) - len(a)
        print(s)
        continue

    else:
        print(1)
        continue

