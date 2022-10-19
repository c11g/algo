# https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    
    for command in commands:
        i,j,k = command
        li = array[i-1:j]
        li.sort()
        
        answer.append(li[k-1])
        
    return answer