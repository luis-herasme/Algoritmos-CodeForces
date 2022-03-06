import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

t = int(input())

for _ in range(t):

    keyboard = input()
    keyboard = keyboard[:-1]
    idx = list(range(len(keyboard)))
    zip_iterator = zip(keyboard, idx)
    keyboard_dictionary = dict(zip_iterator)
    word = input()
    word = word[:-1]

    total = 0
    for i in range(1, len(word)): 
        letter_position1 = keyboard_dictionary[word[i]]
        letter_position2 = keyboard_dictionary[word[i - 1]]
        total += abs(letter_position1 - letter_position2)
    print(total)
