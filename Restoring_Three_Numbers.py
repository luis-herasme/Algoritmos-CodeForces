import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

cuatro = input_list_numbers()

abc = max(cuatro) # a+b+c

del cuatro[cuatro.index(abc)]

ab = cuatro[0] #  a+b, a+c, b+c and a+b+c
ac = cuatro[1]
bc = cuatro[2]

b_c = ab - ac

b = (b_c + bc) / 2
c = bc - b
a = abc - b - c

print(int(a), int(b), int(c))
