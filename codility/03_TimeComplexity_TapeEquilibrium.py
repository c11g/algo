# https://app.codility.com/demo/results/training7GTH8P-7QB/

def solution(A):
    total = sum(A)
    a_sum = 0
    
    diff = []
    for i,v in enumerate(A):
        if (len(A)-1 == i): break
        a_sum += v
        b_sum = total - a_sum
        diff.append(abs(a_sum - b_sum))
    
    return min(diff)