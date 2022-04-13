
f = open("quick_sort_numbers.txt", "r")
content = f.read()
content = content.split('\n')
for i in range(len(content)):
    content[i] = int(content[i])

INPUT = content

def get_median(low, mid, high):
    if high < low < mid:
        return 'low'
    if mid < low < high:
        return 'low'

    if high < mid < low:
        return 'mid'
    if low < mid < high:
        return 'mid'

    if mid < high < low:
        return 'high'
    if low < high < mid:
        return 'high'
        

def partition(A, l, r):
    
    middle = (r - l - 1) // 2 + l
    median = get_median(A[l], A[middle], A[r - 1])
    if median == 'high':
        A[r - 1], A[l] = A[l], A[r - 1]
    elif median == 'mid':
        A[middle], A[l] = A[l], A[middle]    

    # A[r - 1], A[l] = A[l], A[r - 1]
    p = A[l]
    i = l + 1
    for j in range(l, r):
        if A[j] < p:
            A[j], A[i] = A[i], A[j]
            i = i + 1
    A[l], A[i - 1] = A[i - 1], A[l]
    return i

def quick_sort(A, start, stop):
    comparisons = stop - start - 1

    if (stop - start) <= 1:
        return 0

    pi = partition(A, start, stop)
    comparisons_call_1 = quick_sort(A, start, pi - 1)
    comparisons_call_2 = quick_sort(A, pi, stop)

    return comparisons + comparisons_call_1 + comparisons_call_2

c = quick_sort(INPUT, 0, len(INPUT))
print('comparisons: ', c)

for c in range(1, len(INPUT)):
    if INPUT[c - 1] > INPUT[c]:
        print("ERROR")
        break