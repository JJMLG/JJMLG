from collections import deque

def solution(cards1, cards2, goal):
    answer = ''
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    result = []
    for word in goal:
        flag = 0
        cnt = 0
        # while True:
        if cards1 and cards1[0] == word:
            result.append(cards1.popleft())
            flag = 1


        if cards2 and cards2[0] == word:
            result.append(cards2.popleft())
            flag = 1
            # if flag == 0:
            #     break    
    if result == goal:     
        return "Yes"
    else:
    
        return "No"