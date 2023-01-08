# import sys
from collections import deque
tc= int(input())

for T in range(tc):
    que = deque()
    N, M = map(int, input().split())
    x = list(map(int, input().split()))
    # 출력순서
    orderCount = 0
    findDoc = 0
    # 내가 찾아야할 문서를 기록해주고 계산할 수 있게 float 형변환
    for i in range(len(x)):
        if i == M:
            que.append(float(x[i]))
            findDoc = float(x[i])
        else:
            que.append(x[i])
    # 만약 들어온게 한개면 그대로 출력하면 되니까
    if N == 1:
        print(1)
    # 문서 수가 여러장이면
    else:
        while que:
            # 남은게 하나면 출력
            if len(que) ==1:
                print(orderCount+1)
                break
            # 하나이상이면
            else:
                # 남은 문서들의 중요도가 다 같다면 순서대로 출력하면 되니까
                sameDocExist = 0
                # 남은문서들이 다 같은 중요도 인지 확인
                for i in range(len(que)-1):
                    # 같으면 1
                    if que[i] == que[i+1]:
                        sameDocExist = 1
                    #  아니면 0
                    else:
                        sameDocExist = 0
                        break
                    #   일단 내가 찾을 문서가 어딨는지 인덱스 찾기
                # 만약 중요도가 다 같은 문서만 남았다면
                if sameDocExist == 1:
                    for i in range(len(que)):
                        if type(que[i]) == type(findDoc):
                            print(orderCount + i + 1)
                            break
                    break
                else:
                # 지금 내가 확인해야할 문서 pop
                    nowDoc = que.popleft()
                # 근데 이문서가  내가 찾아야할 문서 (float 형태)
                    if type(nowDoc) == float:
                        # print(3)
                        # 그 앞자리가 중
                        # tempCount = 0
                        # que안에 젤 큰수보다 크거나 같다면출력
                        if nowDoc>=max(que):
                            orderCount+=1
                            print(orderCount)
                            break
                        #  아니면 추가
                        else:
                            que.append(nowDoc)
                    # 내가 뽑을 숫자는 아님
                    else:
                        if nowDoc>=max(que):
                            orderCount+=1
                        else:
                            que.append(nowDoc)

