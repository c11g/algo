# https://app.codility.com/demo/results/trainingWZV9KY-5MK/

def solution(A):
    l = len(A)
    if l < 3: return 0
    A.sort()
    for i in range(l-2):
        if A[i] + A[i+1] > A[i+2]:
            return 1
        else:
            continue
    return 0