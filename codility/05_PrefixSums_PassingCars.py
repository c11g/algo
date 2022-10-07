# https://app.codility.com/demo/results/trainingPR98CU-RJ7/

def solution(A):    
    total = 0
    prefix = 0
    for v in A:
        if (v == 0):
            prefix += 1
        else:
            total += prefix
            
    return -1 if total > 1000000000 else total