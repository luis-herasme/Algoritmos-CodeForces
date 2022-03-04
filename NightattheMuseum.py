import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

abc = "abcdefghijklmnopqrstuvwxyz"
idx = list(range(len(abc)))
zip_iterator = zip(abc, idx)
abc_dictionary = dict(zip_iterator)

text = input()
text = text[:-1]
text = 'a' + text
text_idx = [None] * len(text)

for i, l in enumerate(text):
    text_idx[i] = abc_dictionary[l]

total_rotations = 0

for i in range(1, len(text_idx)):
    d1 = abs((text_idx[i - 1] + len(abc)) - text_idx[i])
    d2 = abs(text_idx[i - 1] - (text_idx[i] + len(abc)))
    d3 = abs(text_idx[i - 1] - text_idx[i])

    total_rotations += min(d1, d2, d3)

print(total_rotations)

