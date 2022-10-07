# https://app.codility.com/demo/results/trainingY3YAHG-N8R/

def solution(X, A):
    result = [0 for x in range(X)]
    total = 0

    for sec, pos in enumerate(A):
        if (result[pos-1] == 0):
            result[pos-1] = 1
            total += 1
        if (total == X):
            return sec

    return -1