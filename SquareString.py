import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

t = int(input())

for _ in range(t):
    text = input()
    text = text[: -1]
    if len(text) % 2:
        print("NO")
    else:
        square = True
        for i in range(len(text) // 2):
            if text[i] != text[ i + len(text) // 2]:
                square = False
                break
        if square:
            print("YES")
        else:
            print("NO")
        
