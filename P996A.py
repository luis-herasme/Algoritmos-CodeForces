import sys, math
input = sys.stdin.readline

nBills = 0
bills = [100, 20, 10, 5, 1]
money = int(input())

for bill in bills:
    nBills += math.floor(money/bill)
    money = money%bill

print(nBills)