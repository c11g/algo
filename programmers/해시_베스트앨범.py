# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    half = len(nums) // 2
    nums = len(set(nums))
    return min(half, nums)