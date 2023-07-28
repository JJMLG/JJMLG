"""
일렬로 줄을 세우는 경우는 총 n!
result에 담기는 맨 처음 수는 k // (n - 1) + 1
처음 수가 담기면, 일렬로 다시 세우는 경우를 반복. 이때 n은 n - 1, k는 k % (n - 1)!
"""

def facto(n):
    if n < 1:
        return 1
    else:
        # print(n)
        return n * facto(n - 1)


def solution(n, k):
    answer = []

    arr = list(range(1, n + 1))

    while n != 0:
        num_case = facto(n - 1)
        # print(num_case)
        idx = k // num_case
        k = k % num_case
        if k == 0:
            answer.append(arr.pop(idx - 1))
        else:
            answer.append(arr.pop(idx))
        n -= 1

    return answer