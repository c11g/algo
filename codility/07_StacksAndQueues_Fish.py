# https://app.codility.com/demo/results/trainingX6YUME-ZGE/

def solution(A, B):
    li = [(v, B[i]) for i, v in enumerate(A)]
    
    count = 0
    left = []
    for v, d in li:
        if d == 0:
            while True:
                if len(left) == 0:
                    count += 1
                    break
                elif left[-1] > v: break
                else: left.pop()
        else: left.append(v)

    return count + len(left)