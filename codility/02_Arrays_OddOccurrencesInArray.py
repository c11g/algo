# https://app.codility.com/demo/results/trainingDA6P3W-3GR/

def solution(A):
    A.sort()
    prev = None
    for i, v in enumerate(A):
        if (i % 2 == 0):
            prev = v
        else:
            if (prev != v): break
        
    return prev