# https://app.codility.com/demo/results/training2KW4FB-4D2/

def matching(a, b):
    return (a == '(' and b == ')') or (a == '{' and b == '}') or (a == '[' and b == ']')

def solution(S):
    l = len(S)
    if l % 2 != 0: return 0
    
    left = []
    for v in S:
        if len(left) > 0 and matching(left[-1], v):
            left.pop()
            continue
        
        left.append(v)

    
    return 1 if len(left) == 0 else 0