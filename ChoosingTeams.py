from math import floor
import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

[n, k] = input_list_numbers()
y = input_list_numbers()

valid_students = 0
for i in range(len(y)):
    y[i] = y[i] + k
    if y[i] <= 5:
        valid_students += 1
print(floor(valid_students/3))