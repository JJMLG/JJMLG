def solution(N, stages):
    answer = []
    temp = []
    for i in range(1,N+1):
        bunja = 0
        bunmo = 0
        for j in range(len(stages)):
            if stages[j] >= i:
                       bunmo += 1
            if stages[j] == i:
                       bunja += 1
        
        if bunja ==0 and bunmo == 0:
            temp.append((0,i))
        else:
            percentage = bunja/bunmo
            temp.append((percentage,i))

    temp.sort(key=lambda x: (-x[0], x[1]))
    for k in range(len(temp)):
        answer.append(temp[k][1])
    return answer