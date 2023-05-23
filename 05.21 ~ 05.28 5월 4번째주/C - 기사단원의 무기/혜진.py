def solution(number, limit, power):
    ans = [0] * (number + 1)                    # 1번부터니까 편하게 + 1 해줌
    for n in range(1, number + 1):
        cnt = 0                                 # 약수의 개수
        for i in range(1, int(n**0.5) + 1):
            if i * i == n:                      # 제곱근은 하나
                cnt += 1
            elif n % i == 0:                    # 나머지 약수는 두개
                cnt += 2

            if cnt > limit:                     # 이미 초과했으면 반복문 빨리 끝내기
                break
        ans[n] = power if cnt > limit else cnt  # 초과했으면 power, 아니면 cnt

    return sum(ans)
