import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

a =  input_list_numbers()
s = input()
s = s[:-1] # Remove \n

r = 0

for si in s:
    r += a[int(si) - 1]

print(r)