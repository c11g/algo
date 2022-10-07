# https://app.codility.com/demo/results/trainingX3CRA2-ATF/

def solution(A):
    A.sort()
    for i,v in enumerate(A):
        if v != i+1:
            return v-1
    
    return len(A) + 1