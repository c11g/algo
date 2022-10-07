# https://app.codility.com/demo/results/trainingJ38KMR-MY7/

def solution(N, A):
    result = [0 for _ in range(N)]

    max_v = 0
    max_temp = 0
    for v in A:
        if v == N+1:
            max_v = max_temp
        else:
            result[v-1] = max(result[v-1], max_v) + 1
            max_temp = max( max_temp, result[v-1] )
    
    for i, v in enumerate(result):
        result[i] = max(v, max_v)
    
    return result