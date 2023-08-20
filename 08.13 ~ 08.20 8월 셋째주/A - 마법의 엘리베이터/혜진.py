def solution(storey):
    ans = 0
    while storey:
        move = storey % 10              # 끝 자리부터 0으로 만들어 나가야 한다
        # tmp, move = divmod(storey, 10)
        if move < 5:                    # 5보다 작으면 -로 0 만들기
            ans += move
            storey -= move
        elif move > 5 :                 # 크면 +로 0 만들기
            ans += (10 - move)
            storey += (10 - move)
        else:                           # 5면 그 앞 숫자를 기준으로 해야 함
            tmp = storey // 10
            if tmp % 10 < 5:            # 앞 숫자가 5보다 작으면 -로 0 만들기
                ans += move
                storey -= move
            else:                       #  같거나 크면 +로 0 만들기
                ans += (10 - move)
                storey += (10 - move)
        storey  //= 10
        # storey = tmp
        
    return ans
