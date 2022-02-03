import sys
input = sys.stdin.readline

t = int(input())
ns = [None] * t

for i in range(t):
    ns[i] = int(input())

# x_times is the integral of the coeficients of x + 2x + 4x ... + 2^(k-1)x
x_times = [None] * 30  # log2(10^9) = 29 (n < 10^9)

for i in range(len(x_times)):
    if i == 0:
        x_times[i] = 1
    else:
        x_times[i] = x_times[i - 1] + 2**i

for n in ns:
    k = 2 # k - 1, is the argument of the function x_times
    while True:
        if (n % x_times[k - 1]) == 0:
            print(int(n/x_times[k - 1]))
            break
        k = k + 1