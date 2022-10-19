# https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    answer = ''
    
    participant.sort()
    completion.sort()
    
    for i, v in enumerate(participant):
        if i == len(completion) or completion[i] != v:
            answer = v
            break

    return answer