from itertools import combinations as comb

coordinate = [None, 
    (0, 0), (0, 1), (0, 2),
    (1, 0), (1, 1), (1, 2),
    (2, 0), (2, 1), (2, 2),
] # 3x3 사각형의 좌표들
dy, dx = [0, -1, 1, 0, 0], [0, 0, 0, -1, 1] # 자기 자신 + 상하좌우

P = int(input())
for p in range(P):
    answer = [list(input()) for _ in range(3)] # 정답 배열
    result = 0 # 최소 클릭 횟수
    for i in range(1, 10): # 누르는 횟수 1부터 9까지 브루트포스
        tmp = list(comb(range(1, 10), i)) # i번 누를 때 나올 수 있는 조합
        for t in tmp: # 클릭할 수 있는 조합들 중에서
            if result: break # 정답을 찾았다면 종료
            arr = [list('.'*3) for _ in range(3)] # 답안지
            for j in t: # 클릭할 수 있는 조합들에서
                coor = coordinate[j] # 클릭할 좌표
                y, x = coor[0], coor[1] # 좌표의 y, x
                for k in range(5): # 자기 자신과 상하좌우, 총 5지점의 색을 뒤집는다
                    ny, nx = y+dy[k], x+dx[k] # 색을 뒤집을 좌표들
                    if 0<=ny<3 and 0<=nx<3: # 새로 얻은 좌표들은 사각형 안에 있어야 한다 (3x3 사각형이니 망정이지;;)
                        if arr[ny][nx] == '*': # * -> .
                            arr[ny][nx] = '.'
                        elif arr[ny][nx] == '.': # . -> *
                            arr[ny][nx] = '*'
            flag = True # 구한 답안과 정답을 비교할 것
            for l in range(3):
                if arr[l] != answer[l]: # 답안과 정답이 다른 줄이 나오면 그 답안은 정답이 아님
                    flag = False
            if flag: result = i # 답안의 모든 줄이 정답과 일치하면 해당 클릭 수를 결과로 저장
    print(result)