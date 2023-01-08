def solution(board, moves):
    answer = 0
    stack = []
    ls = [[]]* len(board)
    for i in range(len(board)):
        tmp = []
        for j in range(len(board)):
            board[j][i]
            if board[j][i] == 0:
                continue
            tmp.append(board[j][i])
        ls[i] = tmp
    
    print(ls)
    for i in range(len(moves)):
        if ls[moves[i]-1]:
            tmp = ls[moves[i]-1].pop(0)
            stack.append(tmp)
    

            if len(stack) >= 2:
                if stack[-2] == stack[-1]:
                    stack.pop()
                    stack.pop()
                    answer +=2 
    
    return answer