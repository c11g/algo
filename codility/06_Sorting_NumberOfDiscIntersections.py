# https://app.codility.com/demo/results/trainingB2KZPS-7ST/
# JS: https://app.codility.com/demo/results/trainingNF3DGC-ZPR/

def solution(A):
    li = []
    for i,v in enumerate(A):
        li.append((i-v, 1))
        li.append((i+v, 2))
    
    li.sort()
    
    open_count = 0
    result = 0

    for p in li:
        if (p[1] == 1):
            result += open_count
            open_count += 1
        else:
            open_count -= 1
    
    return result if result <= 10000000 else -1