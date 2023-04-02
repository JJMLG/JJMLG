def solution(common):
    answer = 0

    for i in range(len(common) - 2):
        if common[i + 2] - common[i + 1] == common[i + 1] - common[i]:
            answer = common[-1] + (common[i + 2] - common[i + 1])
        elif common[i + 2] // common[i + 1] == common[i + 1] // common[i]:
            answer = common[-1] * (common[i + 2] // common[i + 1])

    return answer