import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

t = int(input())

for i in range(t):
    [a, b, c, n] = input_list_numbers()
    m = max(a, b, c)
    sister_coins = [a, b, c]

    for coin in range(len(sister_coins)):
        sister_coins[coin] = sister_coins[coin] - m
    
    min_coins_needed = 0
    for coin in range(len(sister_coins)):
        min_coins_needed += abs(sister_coins[coin])

    if n < min_coins_needed:
        print("NO")
    elif n == min_coins_needed:
        print("YES")
    elif n > min_coins_needed:
        if (n - min_coins_needed) % 3 == 0:
            print("YES")
        else:
            print("NO")
