import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

t = int(input())

result = []

for i in range(t):
    n = input()
    n = n[:-1]
    result.append([])

    for (idx, ni) in enumerate(n):
        if ni != "0":
            result[i].append(int(ni) * 10 ** (len(n) - idx - 1))

for n_result in result:
    print(len(n_result))
    print(" ".join(map(str, n_result)))