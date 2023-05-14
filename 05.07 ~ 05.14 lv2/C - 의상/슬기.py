def solution(clothes):
    answer = 1

    cloth = {}

    for i in clothes:
        if i[1] not in cloth:
            cloth[i[1]] = [i[0]]
        else:
            cloth[i[1]].append(i[0])

    for k in cloth.values():
        answer *= len(k) + 1

    return answer - 1