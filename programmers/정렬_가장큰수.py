# https://school.programmers.co.kr/learn/courses/30/lessons/42746

from functools import cmp_to_key

def compare(x, y):
    if x+y > y+x: return -1
    else: return 1

def solution(numbers):
    answer = ''
    s_numbers = [str(x) for x in numbers]
    s_numbers = sorted(s_numbers, key=cmp_to_key(compare))
    answer = ''.join(s_numbers)
    return "0" if int(answer) == 0 else answer