def solution(numbers, hand):
    answer = ''
    keyPad = [[1,2,3], [4,5,6], [7,8,9], ['*', 0,'#']]
    posNum = dict()
    leftThumb = [3,0]
    rightThumb = [3,2]
    for number in numbers:
        for h in range(4):
            for c in range(3):
                if keyPad[h][c]==number:
                    posNum[number]=[h, c]
            #     왼쪽사이드면
                    if c ==0 and h<3:
                        answer+='L'
                        leftThumb = [h,c]
                    elif c== 2 and h<3:
                        answer+='R'
                        rightThumb = [h,c]
                    elif c==1:
            #             같을때
                        if abs(leftThumb[0]- h) + abs(leftThumb[1] - c) == abs(rightThumb[0]- h) + abs(rightThumb[1] - c):
                            if hand=="right":
                                answer+='R'
                                rightThumb = [h,c]
                            else:
                                answer+='L'
                                leftThumb = [h,c]
                        elif abs(leftThumb[0]- h) + abs(leftThumb[1] - c) < abs(rightThumb[0]- h) + abs(rightThumb[1] - c):
                            answer+='L'
                            leftThumb = [h,c]
                        else:
                            answer+='R'
                            rightThumb = [h,c]
    return answer