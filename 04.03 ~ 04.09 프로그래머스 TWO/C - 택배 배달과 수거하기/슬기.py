def solution(cap, n, deliveries, pickups):

    # 한번에 최대한 멀리가서 멀리 있는 곳들의 작업을 먼저 끝내야지
    # 이동횟수를 최소한으로 만들 수 있으므로 입력받은 배열들을 역순으로 뒤집어준다.
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    answer = 0

    have_to_deli = 0
    have_to_pick = 0

    for i in range(n):
        have_to_deli += deliveries[i]
        have_to_pick += pickups[i]

        # 연산의 결과들이 모두 음수라면 해당 위치의 배달/픽업 값이 한번에 실어 나를 수 있는 용량(=cap)보다 적은 것이므로,
        # 오가는 길에 겸사겸사 추가적으로 배달/픽업이 가능
        while have_to_deli > 0 or have_to_pick > 0:
            have_to_deli -= cap
            have_to_pick -= cap
            answer += (n - i) * 2   # 어차피 한번 가면 다시 물류창고로 되돌아와야 하므로 정답에는 거리 x 2

    return answer