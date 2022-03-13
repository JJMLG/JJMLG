"""
arr = 원본 배열
result = 연산을 실행한 배열
매 연산마다 배열을 돌리고
result를 다시 arr에 deepcopy하면서 진행
"""

import copy # deepcopy 사용

def one():
    global arr, result
    result = []
    for a in arr[::-1]: # 세로로 뒤집어서
        result.append(a) # 한 줄 씩 추가
    arr = copy.deepcopy(result) # arr에 result 덮어쓰기

def two():
    global arr, result
    result = []
    for a in arr:
        result.append(a[::-1]) # 가로로 뒤집어서 한 줄 씩 추가
    arr = copy.deepcopy(result) # arr에 result 덮어쓰기
    
def three():
    global arr, result
    result = []
    for j in range(M): # 왼쪽 줄을
        tmp = []
        for i in range(N-1, -1, -1): # 거꾸로 읽어와서
            tmp.append(arr[i][j])
        result.append(tmp) # 한 줄 씩 추가
    arr = copy.deepcopy(result) # arr에 result 덮어쓰기

def four():
    global arr, result
    result = []
    for j in range(M-1, -1, -1): # 오른쪽 줄을
        tmp = []
        for i in range(N): # 읽어와서
            tmp.append(arr[i][j])
        result.append(tmp) # 한 줄 씩 추가
    arr = copy.deepcopy(result) # arr에 result 덮어쓰기

"""
5번연산, 6번연산은
배열의 모양을 
1 2
4 3
으로 나누어 생각하기로 함
5번연산을 실행한 결과값의 맨 윗줄은
4번의 첫 줄 + 1번의 첫 줄이 되고
그렇게 결과값의 반을 채우고 나면 나머지 반은
3번의 첫 줄 + 2번의 첫 줄
을 더한 값으로 순서대로 나머지 반을 채우게 됨
"""
def five():
    global arr, result
    result = []
    for i in range(N//2, N):
        tmp1 = [] # 4
        tmp2 = [] # 1
        for j in range(M//2):
            tmp1.append(arr[i][j])
            tmp2.append(arr[i-(N//2)][j])
        result.append(tmp1+tmp2) # 4와 1을 한 줄 씩 더해서 result에 추가
    for i in range(N//2, N):
        tmp1 = [] # 3
        tmp2 = [] # 2
        for j in range(M//2, M):
            tmp1.append(arr[i][j])
            tmp2.append(arr[i-(N//2)][j])
        result.append(tmp1+tmp2) # 3과 2를 한 줄 씩 더해서 result에 추가
    arr = copy.deepcopy(result) # arr에 result 덮어쓰기

"""
6번연산은
2번의 첫 줄 + 3번의 첫 줄
을 구해서 결과값의 절반을 채우고
나머지 절반은
1번의 첫 줄 + 4번의 첫 줄
을 더한 값으로 채움
"""
def six():
    global arr, result
    result = []
    for i in range(N//2):
        tmp1 = [] # 2
        tmp2 = [] # 3
        for j in range(M//2, M):
            tmp1.append(arr[i][j])
            tmp2.append(arr[i+(N//2)][j])
        result.append(tmp1+tmp2)    
    for i in range(N//2):
        tmp1 = [] # 1
        tmp2 = [] # 4
        for j in range(M//2):
            tmp1.append(arr[i][j])
            tmp2.append(arr[i+(N//2)][j])
        result.append(tmp1+tmp2)
    arr = copy.deepcopy(result) # arr에 result 덮어쓰기


N, M, R = map(int, input().split())
arr = [] # 원본 배열
for n in range(N):
    arr.append(list(map(int, input().split())))
orders = list(map(int, input().split())) # 연산들
result = [] # 연산을 진행할 배열

for order in orders:
    if order == 1:
        one()
    elif order == 2:
        two()
    elif order == 3:
        three()
        N, M = M, N # 직사각형 배열인 경우 에러 방지
    elif order == 4:
        four()        
        N, M = M, N # 직사각형 배열인 경우 에러 방지
    elif order == 5:
        five()
    elif order == 6:
        six()

for r in result:
    print(*r) # 각 줄 출력