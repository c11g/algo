# https://app.codility.com/demo/results/training3TM5DN-VPU/

def solution(A, K):
    if (len(A) != 0):
        for i in range(K):
            last = A.pop()
            A.insert(0, last)

    return A