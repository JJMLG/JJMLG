def solution(sequence, k):
    ans = []
    L = len(sequence)
    n = sequence[0]
    idx = 0

    # 시작인덱스가 i, 끝인덱스가 idx -> 길이는 idx - i
    for i, v in enumerate(sequence):
        while n < k and idx < L - 1:
            idx += 1
            n += sequence[idx]
        if n == k:
            ans.append([idx - i, [i, idx]])
        n -= v
        
    ans.sort()
    return ans[0][1]


print(solution([1, 2, 3, 4, 5], 7))
print(solution([1, 1, 1, 2, 3, 4, 5], 5))
print(solution([2, 2, 2, 2, 2], 6))
