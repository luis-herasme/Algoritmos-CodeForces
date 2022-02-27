import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

t = int(input())

for i in range(t):
    s = input_list_numbers()
    
    finalist1 = 0
    finalist2 = 0

    if s[0] > s[1]:
        finalist1 = s[0]
    else:
        finalist1 = s[1]

    if s[2] > s[3]:
        finalist2 = s[2]
    else:
        finalist2 = s[3]

    s_order = s.copy()
    s.sort()
    max_skill = s[-1]
    second_max_skill = s[-2]

    if (finalist2 == max_skill or finalist2 == second_max_skill):
        if (finalist1 == max_skill or finalist1 == second_max_skill):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")