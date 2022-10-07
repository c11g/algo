# https://app.codility.com/demo/results/trainingQ8UGF2-ERD/

def solution(H):
    result = 0
    stack = []
    for v in H:
        if len(stack) == 0 or v > stack[-1]:
            stack.append(v)
            result += 1
            continue
        if v == stack[-1]: continue

        while True:
            if len(stack) == 0 or v > stack[-1]:
                stack.append(v)
                result += 1
                break
            if v == stack[-1]: break
            else: stack.pop()
    
    return result