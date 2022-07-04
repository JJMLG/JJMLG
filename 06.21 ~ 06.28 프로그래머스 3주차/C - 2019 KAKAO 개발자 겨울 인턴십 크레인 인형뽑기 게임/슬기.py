
board = [
 [0, 0, 0, 0, 0],
 [0, 0, 1, 0, 3],
 [0, 2, 5, 0, 1],
 [4, 2, 4, 4, 2],
 [3, 5, 1, 3, 1]
]

moves = [1, 5, 3, 5, 1, 2, 1, 4]

def solution(board, moves):
    answer = 0
    # print(board)
    basket = []
    for k in range(len(moves)):
        # print(k)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != 0 and moves[k] == j+1:
                    basket.append(board[i][moves[k]-1])
                    board[i][moves[k]-1] = 0
                    pass
                pass
    print(basket, '------ㅇㅕ기-------')
    return answer

print(solution(board, moves))


"""
# 보드는 인형위치, moves는 뽑을 인형 위치
1. 인형을 뽑아 준다 (돌다가 x 좌표에 인형 있으면 pop?)
2. 새로운 list(바구니)에 담아준다(바구니에 append)
3. 똑같은 두 개가 만나면 cnt 2가 되면 pop 하고 answer += 1 해주기

# moves의 번호는 (x,y)면 x를 가리킴?
"""