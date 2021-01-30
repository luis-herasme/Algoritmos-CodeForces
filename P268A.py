import sys
input = sys.stdin.readline

def inlt():
    return(list(map(int, input().split())))

nTeams = int(input())
Teams = [0] * nTeams
change = 0

for i in range(nTeams):
    [guest, home] = inlt()
    Teams[i] = [guest, home]

for i in range(len(Teams)):
    for i2 in range(len(Teams)):
        if i != i2:
            if Teams[i][0] == Teams[i2][1]:
                change += 1

print(change)