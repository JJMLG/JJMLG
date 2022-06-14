def solution(lottos, win_nums):
    lottos = sorted(lottos)
    win_nums = sorted(win_nums)
    print(lottos, win_nums)
    #     rank는 일차하는 숫자 인덱스에 값이 순위
    rank = [6, 6, 5, 4, 3, 2, 1]

    # 일치하는 갯수 cnt
    cnt = 0
    # 0의 갯수
    zero_cnt = 0
    for i in lottos:
        # 만약에 0이 아니고 당첨 숫자에 있다면
        if i != 0 and i in win_nums:
            cnt += 1
        # 만약에 0이면 0 갯수
        if i == 0:
            zero_cnt += 1
    # 최고 당첨 순위, 최저 당첨 순위
    answer = [rank[cnt + zero_cnt], rank[cnt]]

    return answer