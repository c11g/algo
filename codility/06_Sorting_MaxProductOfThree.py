# https://app.codility.com/demo/results/training9VWMFT-WUZ/

def solution(A):
    A.sort()
    if (A[0] > -1 or A[-1] < 1):
        return A[-1] * A[-2] * A[-3]
    else:
        return A[-1] * max(A[-2] * A[-3], A[0] * A[1])