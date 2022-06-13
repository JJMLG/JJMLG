def solution(lottos, win_nums):
    lottos = sorted(lottos)
    win_nums = sorted(win_nums)
    rank = [6, 6, 5, 4, 3, 2, 1]
    cnt = 0
    zero_cnt = 0
    for i in lottos:
        if i != 0 and i in win_nums:
            cnt += 1
        if i == 0:
            zero_cnt += 1

    answer = [rank[cnt + zero_cnt], rank[cnt]]

    return answer