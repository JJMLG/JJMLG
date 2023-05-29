def solution(n, lost, reserve):
    answer = 0

    n_lost = set(lost) - set(reserve)
    n_reserve = set(reserve) - set(lost)
    for x in n_lost:
        # 조건절을 쓸 때 x-1부터 탐색하도록 해야 함
        if x - 1 in n_reserve:
            n_reserve.remove(x - 1)
        # if가 아니라면 x+1 탐색
        elif x + 1 in n_reserve:
            n_reserve.remove(x + 1)
        # 둘다 해당 안되면 체육복을 빌릴 수가 없음
        else:
            n -= 1

    return answer