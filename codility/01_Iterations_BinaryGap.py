# https://app.codility.com/demo/results/training73HG82-P6W/

def solution(N):
    binary_list = list((bin(N)[2:]))
    length = len(binary_list)
    
    result = 0
    temp = 0

    i = 0
    while i < length:
        if (binary_list[i] == '1'):
            result = max(result, temp)
            if (result == length - (i+1)): break
            temp = 0
        else:
            temp = temp + 1

        i = i + 1

    return result