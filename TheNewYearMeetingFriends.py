
import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

xs = input_list_numbers()
total_distances = []

for point_encounter in range(min(xs), max(xs)):
    total_distance = 0
    for x in xs:
        total_distance += abs(point_encounter - x)
    total_distances.append(total_distance)

print(int(min(total_distances)))
