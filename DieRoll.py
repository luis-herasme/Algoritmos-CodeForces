from fractions import Fraction
import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

[Y, W] = input_list_numbers()

h = max(Y, W)

d = 6 - (h - 1)

if (str(Fraction(d/6)) == "1"):
    print("1/1")
else:
    print(str(Fraction(d, 6)))
