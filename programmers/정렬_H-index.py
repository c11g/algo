# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations.sort()
    
    n = len(citations)
    h = min(n, citations[0])
    
    for i,v in enumerate(citations):
        new_h = min(v, n-i)
        if new_h < h: break
        h = new_h
    
    return h