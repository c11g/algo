# https://app.codility.com/demo/results/trainingXMX347-3FU/

def solution(A):
    A.sort()
    
    prev = None
    curr = 1
    for v in A:
        if v < 1: continue
        if v == prev: continue
        
        prev = v
        if v == curr:
            curr += 1
        else:
            return curr
    
    return prev+1 if prev else 1