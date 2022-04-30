import sys
from collections import deque

def input():
    return sys.stdin.readline()

for t in range(int(input())):
    result = 1 # 인쇄 순서 초기화
    N, M = map(int, input().split())
    tmp = list(map(int, input().split())) # 문서 중요도 입력
    docs = deque() # popleft() 사용할 것
    i = 0 # 문서의 순서
    for tm in tmp:
        docs.append((tm, i)) # 현재 문서의 (중요도, 순서) 를 담은 리스트
        i += 1
    # print(docs) # 디버깅
    while docs: # 
        tmp = [] # 문서의 중요도들만을 담을 리스트
        for i in range(len(docs)):
            tmp.append(docs[i][0])
        if docs[0][0] != max(tmp): # 가장 중요도가 높은 문서가 아니라면
            docs.append(docs.popleft()) # 해당 문서를 가장 뒤로 이동
        else: # 가장 중요도가 높은 문서라면
            if M == docs[0][1]: # 구하고자 하는 인쇄순서의 문서라면
                break # 종료하고
            docs.popleft() # 인쇄
            result += 1 # 인쇄순서 +1
    print(result) # 현재 인쇄순서 번호를 출력