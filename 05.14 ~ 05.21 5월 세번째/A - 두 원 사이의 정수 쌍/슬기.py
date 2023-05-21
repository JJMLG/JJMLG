def solution(r1, r2):
    answer = 0
    minY, maxY = r1, r2  # 최소, 최대로 가질 수 있는 y좌표
    # 1사분면에 대해서만 좌표값을 구하고 대칭이므로 *4한다.
    for x in range(0, r2):
        while r2 ** 2 < maxY ** 2 + x ** 2:
            maxY -= 1
        # minY 양수값을 유지
        while minY - 1 and r1 ** 2 <= (minY - 1) ** 2 + x ** 2:
            minY -= 1
        answer += (maxY - minY) + 1

    return answer * 4