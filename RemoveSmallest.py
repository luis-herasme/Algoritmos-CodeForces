import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

t = int(input())
result = [None] * t

for i in range(t):
    n = int(input())
    a = input_list_numbers()
    
    if n == 1:
        result[i] = "YES"
        continue
    
    a.sort()
    a_drvt = [None] * ( len(a) - 1)

    for j in range(1, len(a)):
        a_drvt[j - 1] = a[j] - a[j - 1] 
    
    if max(a_drvt) > 1:
        result[i] = "NO"
    else:
        result[i] = "YES"

for i in result:
    print(i)
