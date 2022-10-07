# https://app.codility.com/demo/results/training8PUTBV-94W/

def solution(S):
    l = len(S)
    if l % 2 != 0: return 0
    
    left = []
    for c in S:
        if len(left) > 0 and left[-1] == '(' and c == ')': left.pop()
        else: left.append(c)
    
    return 1 if len(left) == 0 else 0