# https://app.codility.com/demo/results/training2F4HEM-NVQ/

# 아이디어
# 구간 탐색이긴 하나, 모든 구간을 볼 필요 없이 실질적으로 2개 또는 3개의 연속된 구간에서 최소 평균 값을 찾을 수 있다.
# 4개 이상의 구간의 평균A는 구간을 2개 이상으로 나눌 경우 각 구간의 평균이 A와 같거나 A보다 큰 경우 + A보다 작은 경우의 조합이므로, 2개 또는 3개 구간에서 최솟 값을 찾을 수 있다.
# 최소 평균 값이 3개인 경우는 [3, 5, 2] 처럼 중간 값이 크고 세번 째 값이 가장 작은 값이 나올 경우다.
# 즉, 리스트를 순회하면서 각 요소마다 2, 3개 구간의 평균 값을 확인 후 기존 평균 값보다 작으면 업데이트!

def solution(A):
    n = len(A)

    result = 0
    min_avg = (A[0] + A[1] ) / 2
    for i in range(1, n-1):
        curr = A[i]

        j = A[i+1]
        avg2 = (curr + j) / 2
        curr_avg = min(min_avg, avg2)

        if i < n - 2:
            k = A[i+2]
            avg3 = (curr + j + k) / 3
            curr_avg = min(curr_avg, avg3)

        if min_avg > curr_avg:
            min_avg = curr_avg
            result = i

    return result