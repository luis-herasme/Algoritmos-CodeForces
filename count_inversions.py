import math


INPUT = [1, 9, 6, 4, 5]

def count_split_inv(B, C):
    D = [None] * ( len(B) + len(C) )
    i = 0
    j = 0
    inversions = 0

    B.append(math.inf)
    C.append(math.inf)

    for k in range(len(D)):

        if B[i] < C[j]:
                D[k] = B[i]
                i = i + 1

        elif B[i] > C[j]:
            D[k] = C[j]
            j = j + 1

            inversions = inversions + (len(B) - (i + 1))

    return (D, inversions)

def sort_and_count(A):
    if len(A) == 1:
        return (A, 0)
    else:
        (B, X) = sort_and_count(A[: len(A) // 2])
        (C, Y) = sort_and_count(A[len(A) // 2: ])
        (D, Z) = count_split_inv(B, C)

    return (D, X + Y + Z)

f = open("array.txt", "r")
content = f.read()
content = content.split('\n')
for i in range(len(content)):
    content[i] = int(content[i])

print(sort_and_count(content))