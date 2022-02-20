import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

[n, m] = input_list_numbers()

black_and_white = True
for i in range(n):
    pixels_row = input()[:-1]
    pixels_row = pixels_row.split(" ")

    for j in pixels_row:
        if j == 'C' or j == 'M' or j == 'Y':
            black_and_white = False
            break

if black_and_white:
    print("#Black&White")
else:
    print("#Color")
