"""
바구니 = 스택 
크레인만 구현하면 됌
"""
def solution(board, moves):
    answer = 0
    bucket = [] # 바구니
    for i in range(len(moves)): # 인덱스 맞추기
        moves[i] -= 1
    for i in range(len(moves)): # 크레인이 내려가면서
        for j in range(len(board)): # 보드를 확인
            tmp = board[j][moves[i]] # 현재 크레인 위치
            if tmp: # 인형이 있다?
                board[j][moves[i]] = 0 # 인형을 꺼내서
                if bucket: # 바구니에 인형이 있다?
                    if bucket[-1] == tmp: # 꺼낸 인형과 바구니 맨 위 인형이 같다?
                        bucket.pop() # !팝!
                        answer += 2 # 터진 인형 +2
                    else: # 꺼낸 인형과 바구니 맨 위 인형이 다르다?
                        bucket.append(tmp) # 인형 집어넣기
                else: # 바구니가 비었다?
                    bucket.append(tmp)
                break # 크레인 무빙 한 번에 인형 하나만 가능
    return answer