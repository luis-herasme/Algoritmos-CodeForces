import sys
input = sys.stdin.readline

m = [0] * 1001
m[1] = 1
last_idx = 1

def getNumberAtIdx(idx):
    global last_idx, m
    n = m[last_idx]

    while True:
        if m[idx]:
            return m[idx]
        n = n + 1
        if (n % 3 != 0) and (n % 10 != 3):
            last_idx = last_idx + 1
            m[last_idx] = n


t = int(input())
k_list = [None] * t

for i in range(t):
    k_list[i] = int(input())

for k in k_list:
    print(getNumberAtIdx(k))
