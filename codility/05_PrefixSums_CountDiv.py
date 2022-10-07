# https://app.codility.com/demo/results/training8HRSVS-RQA/

def solution(A, B, K):
    if K == 1: return B - A + 1
    
    count = 0
    for i in range(A, B+1):
        if i % K == 0:
            count += 1
            A = i
            break
    
    count += (B - A) // K
    
    return count