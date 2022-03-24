import sys
input = sys.stdin.readline
 
def input_list_numbers():
    return(list(map(int, input().split())))

[n, m, k] = input_list_numbers()
if k >= n and m >= n:
    print("Yes")
else:
    print("No")
