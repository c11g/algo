# https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    answer = 1
    
    dict = {}
    for _, key in clothes:
        dict[key] = dict.get(key, 0) + 1
    
    for n in dict.keys():
        answer = answer * (dict[n] + 1)
    
    return answer - 1