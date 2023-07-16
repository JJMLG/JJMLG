def solution(order):
    answer = 0

    stack = []

    #   컨테이너 벨트에서 꺼낼 물건 번호
    put = 1
    for i in order:
        #       메인 컨테이너에 있다면 보조로 보냄
        while put <= i:
            stack.append(put)
            put += 1
        #       보조에 있고 맨위에 있으면 꺼냄
        if stack and stack[-1] == i:
            stack.pop()
            answer += 1
        #       못 꺼내면
        else:
            break

    return answer