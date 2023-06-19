def solution(cards1, cards2, goal):
    i = j = 0
    for g in goal:
        # cards1과 cards2에는 서로 다른 단어만 존재하니까 하나씩 확인하고
        if i < len(cards1) and cards1[i] == g:
            i += 1
        elif j < len(cards2) and cards2[j] == g:
            j += 1
        # 없으면 바로 No
        else:
            return 'No'
    # 반복문 다 돌면 Yes
    return 'Yes'
