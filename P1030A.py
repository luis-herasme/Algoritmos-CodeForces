import sys
input = sys.stdin.readline

def inlt():
    return(list(map(int, input().split())))

n = int(input())
easy = 1
opiniones = inlt()

for i in opiniones:
    if i:
        easy = 0
if easy:
    print('EASY')
else:
    print('HARD')
