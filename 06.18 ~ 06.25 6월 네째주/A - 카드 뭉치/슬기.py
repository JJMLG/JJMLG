def solution(cards1, cards2, goal):
    answer = 'Yes'

    goal_dic = {}

    for idx, val in enumerate(goal):
        goal_dic[val] = idx

    tmp1 = []
    w1 = []
    for i in cards1:
        for k, v in enumerate(goal):
            if v == i:
                tmp1.append(k)
                w1.append(cards1.index(i))

    tmp2 = []
    w2 = []
    for i in cards2:
        for k, v in enumerate(goal):
            if v == i:
                tmp2.append(k)
                w2.append(cards2.index(i))

    check1 = sorted(tmp1)
    check2 = sorted(tmp2)

    # 정렬 값과 순서 다른지 판별
    if tmp1 != check1 or tmp2 != check2:
        answer = 'No'

    # 차례대로 들어가지 않았을 경우
    # 반례  ["a", "b", "c"], ["d", "e", "f"], ["a", "d", "f"]
    if len(w1) != len(cards1) and len(w1) != 1:
        for i in range(len(w1) - 1):
            if w1[i + 1] - w1[i] != 1:
                answer = 'No'
                break

    if len(w2) != len(cards2) and len(w2) != 1:
        for i in range(len(w2) - 1):
            if w2[i + 1] - w2[i] != 1:
                answer = 'No'
                break

    return answer