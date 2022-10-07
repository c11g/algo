# https://app.codility.com/demo/results/trainingDUM7KZ-6GR/

import math

def solution(X, Y, D):
    gap = Y - X
    return math.ceil(gap / D)