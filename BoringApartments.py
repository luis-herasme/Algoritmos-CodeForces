import sys
input = sys.stdin.readline

t = int(input())
x_list = [None] * t

for i in range(t):
    x_list[i] = int(input())

for x in x_list:
    x_first_digit = x % 10
    digits = len(str(x))
    digits_press_for_this_number = digits * (digits + 1) // 2
    print(digits_press_for_this_number + (x_first_digit - 1) * 10)