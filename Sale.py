import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

[ n, m ] = input_list_numbers()
tvs = input_list_numbers()

for i in range(len(tvs)):
    if tvs[i] > 0:
        tvs[i] = 0 

tvs.sort()
print( -1 * sum(tvs[:m]) )
