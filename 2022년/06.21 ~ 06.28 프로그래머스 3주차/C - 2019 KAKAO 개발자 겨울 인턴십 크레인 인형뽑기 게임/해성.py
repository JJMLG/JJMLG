def solution(board, moves):
    answer = 0
    basket = []
    prev = 0
    # 바구니에 넣는 과정
    for i in moves:
        for c in range(len(board)):
            # 해당 인형이 없으면 담걸로 넘어가기
            if board[c][i-1] ==0:
                continue
            # 해당 인형이 있으면
            else:
            # 만약 바스켓에 있으면
                if basket:
                    # 빼서 지금꺼랑 확인
                    prev = basket.pop()
                    # 같으면 터트리기
                    if prev == board[c][i-1]:
                        answer +=2
                    # 다르면 다시 넣고 이번것도 추가
                    else:
                        basket.append(prev)
                        basket.append(board[c][i-1])
                # 바스켓에 암것도 없으면 추가
                else:
                    basket.append(board[c][i-1])
                # 뺐으면 없는걸로 처리
                board[c][i-1]=0
                # break 안해주면 밑에 인형 계속 뽑으니까
                break
    return answer