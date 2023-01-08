"""
숫자가 주어졌을 때
if 숫자가 가장자리(사이드)에 있으면:
    answer += 해당 손
    해당 손 위치 옮겨주기
elif 숫자가 가운데에 있으면(2, 5, 8, 0):
    if 거리가 같으면:
        answer += 해당 손
        해당 손 위치 옮겨주기
    elif 거리가 다르면:
        answer += 해당 손
        해당 손 위치 옮겨주기
"""
def solution(numbers, hand):
    answer = '' # L or R 하나씩 추가
    l = [3, 0] # *에서 시작
    r = [3, 2] # #에서 시작
    key = [3, 1] # 2, 5, 8, 0 일 경우
    keypad = [
        [1, 2, 3],
        [4, 5, 6], 
        [7, 8, 9],
        ['*', 0, '#']
    ] # 숫자패드 배열    
    for num in numbers: # 숫자 입력
        if num in [1, 4, 7]: # 왼손
            answer = answer + 'L'
            for i in range(3): # 해당 위치로 이동
                if keypad[i][0] == num:
                    l = [i, 0]
        elif num in [3, 6, 9]: # 오른손
            answer = answer + 'R'
            for i in range(3): # 해당 위치로 이동
                if keypad[i][2] == num:
                    r = [i, 0]
        else: # 2, 5, 8, 0
            for i in range(4): # num의 좌표 찾기
                if keypad[i][1] == num:
                    key = [i, 1]
            ld = abs(key[0]-l[0]) + abs(key[1]-l[1]) # 왼손으로부터의 거리
            rd = abs(key[0]-r[0]) + abs(key[1]-r[1]) # 오른손으로부터의 거리
            if ld < rd: # 왼손이 더 가까우면
                answer = answer + 'L'
                l = key # 왼손을 이동
            elif ld > rd: # 오른손이 더 가까우면
                answer = answer + 'R'
                r = key # 오른손을 이동
            else: # 거리가 같으면
                main_hand = '' # 주 손 확인
                if hand == 'left': # 왼손잡이면
                    main_hand = 'L'
                    l = key # 왼손을 이동
                elif hand == 'right': # 오른손잡이면
                    main_hand = 'R'
                    r = key # 오른손을 이동
                answer = answer + main_hand # 주 손으로 버튼을 누름
    return answer