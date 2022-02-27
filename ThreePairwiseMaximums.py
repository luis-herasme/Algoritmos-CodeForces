import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

t = int(input())

for i in range(t):
    [x, y, z] = input_list_numbers()

    a = [x, y, 1]
    b = [x, z, 1]
    c = [y, z, 1]
    yes = False
    for ai in a:
        for bi in b:
            for ci in c:
                if x == max(ai, bi) and y == max(ai, ci) and z == max(bi, ci):
                    print("YES")
                    print(ai, bi, ci)
                    yes = True
                    break
            if yes:
                break
        if yes:
            break
    if not yes:
        print("NO")
