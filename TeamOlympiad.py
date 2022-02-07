
import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))


n = int(input())
students = input_list_numbers()

programmers = []
maths = []
PE = []

for idx, student in enumerate(students):
    if student == 1:
        programmers.append(idx + 1)
    elif student == 2:
        maths.append(idx + 1)
    elif student == 3:
        PE.append(idx + 1)

number_of_teams = min(len(programmers), len(maths), len(PE))
print(number_of_teams)

if number_of_teams > 0:
    for i in range(number_of_teams):
        print(programmers[i], maths[i], PE[i])

