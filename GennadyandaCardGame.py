import sys
input = sys.stdin.readline


card_in_table = input()
card_in_table = card_in_table[:-1]

hand = input()
hand = hand[:-1]
hand = hand.split(" ")

printed_yes = False

for card in hand:
    if card[0] == card_in_table[0] or card[1] == card_in_table[1]:
        print("YES")
        printed_yes = True
        break
    
if not printed_yes:
    print("NO")
