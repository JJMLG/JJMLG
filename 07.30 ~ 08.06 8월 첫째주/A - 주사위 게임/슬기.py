def solution(a, b, c, d):
    answer = 0

    dice = [a, b, c, d]
    ddice = {}

    for i in dice:
        if i not in ddice:
            ddice[i] = 1
        else:
            ddice[i] += 1
    print(len(ddice))

    if len(ddice) == 1:
        answer = 1111 * a
    elif len(ddice) == 2:
        if 3 in ddice.values():
            tmp = 0
            for k, v in ddice.items():
                if v >= 3:
                    tmp += 10 * k
                else:
                    tmp += k
            answer = tmp ** 2
        elif 2 in ddice.values():
            tmp = list(ddice.keys())
            answer = sum(tmp) * abs(tmp[0] - tmp[1])
    elif len(ddice) == 3:
        tmp = 1
        for k, v in ddice.items():
            if v != 2:
                tmp *= k
        answer = tmp
    elif len(ddice) == 4:
        answer = min(ddice)

    return answer