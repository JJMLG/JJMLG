def solution(numbers, hand):
    answer = ''
    left_hand = [3,0]
    right_hand = [3,2]
    
    
    for i in range(len(numbers)):
        if numbers[i] in [1,4,7]:
            answer += 'L'
            if numbers[i] == 1:
                left_hand = [0,0]
            if numbers[i] == 4:
                left_hand = [1,0]
            if numbers[i] == 7:
                left_hand = [2,0]
            
        elif numbers[i] in [3,6,9]:
            answer += 'R'
            if numbers[i] == 3:
                right_hand = [0,2]
            if numbers[i] == 6:
                right_hand = [1,2]
            if numbers[i] == 9:
                right_hand = [2,2]
        else:
            if numbers[i] == 2:
                if abs(1-left_hand[1]) + abs(0-left_hand[0]) <  abs(1-right_hand[1]) + abs(0-right_hand[0]):
                    left_hand = [0,1]
                    answer += 'L'
                elif abs(1-left_hand[1]) + abs(0-left_hand[0]) >  abs(1-right_hand[1]) + abs(0-right_hand[0]):
                    right_hand = [0,1]
                    answer += 'R'
                else:
                    if hand == 'left':
                        left_hand = [0,1]
                        answer += 'L'
                    if hand == 'right':
                        right_hand = [0,1]
                        answer += 'R'
            if numbers[i] == 5:
                if abs(1-left_hand[1]) + abs(1-left_hand[0]) <  abs(1-right_hand[1]) + abs(1-right_hand[0]):
                    left_hand = [1,1]
                    answer += 'L'
                elif abs(1-left_hand[1]) + abs(1-left_hand[0]) >  abs(1-right_hand[1]) + abs(1-right_hand[0]):
                    right_hand = [1,1]
                    answer += 'R'
                else:
                    if hand == 'left':
                        left_hand = [1,1]
                        answer += 'L'
                    if hand == 'right':
                        right_hand = [1,1]
                        answer += 'R'
            if numbers[i] == 8:
                if abs(1-left_hand[1]) + abs(2-left_hand[0]) <  abs(1-right_hand[1]) + abs(2-right_hand[0]):
                    left_hand = [2,1]
                    answer += 'L'
                elif abs(1-left_hand[1]) + abs(2-left_hand[0]) >  abs(1-right_hand[1]) + abs(2-right_hand[0]):
                    right_hand = [2,1]
                    answer += 'R'
                else:
                    if hand == 'left':
                        left_hand = [2,1]
                        answer += 'L'
                    if hand == 'right':
                        right_hand = [2,1]
                        answer += 'R'
            if numbers[i] == 0:
                if abs(1-left_hand[1]) + abs(3-left_hand[0]) <  abs(1-right_hand[1]) + abs(3-right_hand[0]):
                    left_hand = [3,1]
                    answer += 'L'
                elif abs(1-left_hand[1]) + abs(3-left_hand[0]) >  abs(1-right_hand[1]) + abs(3-right_hand[0]):
                    right_hand = [3,1]
                    answer += 'R'
                else:
                    if hand == 'left':
                        left_hand = [3,1]
                        answer += 'L'
                    if hand == 'right':
                        right_hand = [3,1]
                        answer += 'R'
        print(left_hand,right_hand)
    return answer