def solution(n, lost, reserve):
    cloth = [0] + [1] * n               # 가진 체육복 수
    for lo in lost: cloth[lo] -= 1
    for re in reserve: cloth[re] += 1

    cnt = 0
    for i in range(1, n + 1):
        if not cloth[i]:                # 체육복 없으면
            if cloth[i - 1] == 2:       # 앞사람 먼저 확인
                cloth[i - 1] -= 1
                cloth[i] += 1
            elif i < n and cloth[i + 1] == 2:   # 앞사람한테 못빌리면 뒷사람 확인
                cloth[i + 1] -= 1
                cloth[i] += 1
        if cloth[i] > 0:
            cnt += 1

    return cnt
