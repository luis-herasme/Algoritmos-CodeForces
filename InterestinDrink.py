import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

n = int(input())
x = input_list_numbers()
x.sort()
q = int(input())
m = [None] * q

for i in range(q):
    m[i] = int(input())

def bs(arr, x):
    r = len(arr) - 1
    l = 0
    answer = False

    while l <= r:
        m = l + (r - l) // 2

        if arr[m] <= x:
            l = m + 1   
        elif arr[m] > x:
            r = m - 1

    if not answer:        
        m = l

        while True:
            if m <= 0:
                if len(arr) > 1:
                    if arr[1] <= x:
                        m = 1
                        continue
                    else:
                        if arr[0] == x:
                            print(1)
                        else:
                            print(0)
                        return
                else:
                    if arr[0] == x:
                        print(1)
                    else:
                        print(0)
                    return
                    
 
            elif m > len(arr) - 1:
                print(len(arr))
                return

            elif m == len(arr) - 1:
                if x >= arr[m]:
                    print(len(arr))
                else:
                    print(len(arr) - 1)
                return

            if m - 1 >= 0 and m + 1 <= len(arr) - 1:
                if (arr[m - 1] <= x) and (x < arr[m + 1]):
                    if arr[m] <= x:
                        print(m + 1)
                    else:
                        print(m)
                    return
                
            if x < arr[m - 1]:
                m = m - 1
                continue

            if x >= arr[m + 1]:
                m = m + 1
                continue


for mi in m:
    bs(x, mi)