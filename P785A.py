import sys
input = sys.stdin.readline

n = int(input())
faces = 0

for i in range(n):
    figure = input()
    figure = figure[:len(figure) - 1]
    if figure == "Tetrahedron":
        faces += 4
    if figure == "Cube":
        faces += 6
    if figure == "Octahedron":
        faces += 8
    if figure == "Dodecahedron":
        faces += 12
    if figure == "Icosahedron":
        faces += 20

print(faces)