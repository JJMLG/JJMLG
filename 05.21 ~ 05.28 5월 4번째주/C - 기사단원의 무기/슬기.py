def solution(number, limit, power):
    answer = 0

    arr = []
    for i in range(1, number + 1):
        cnt = 0
        for j in range(1, int(i ** 0.5) + 1):
            # 제곱근이면 + 1
            if (i == j ** 2):
                # print(i, j**2)
                cnt += 1
            elif i % j == 0:
                cnt += 2
                # print(i, j)
        if cnt > limit:
            arr.append(power)
        else:
            arr.append(cnt)

    answer = sum(arr)

    # 시간초과 코드
    # arr = []
    # for i in range(1, number+1):
    #     tmp = 0
    #     for j in range(1, number+1):
    #         if i % j == 0:
    #             tmp += 1
    #     if tmp > limit:
    #         tmp = power
    #     arr.append(tmp)
    # answer = sum(arr)

    return answer