N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)] # 숫자 배열 입력 받기
for i in range(N, -1, -1): # 가장 큰 정사각형부터 확인
    # 정사각형의 길이가 i+1 일 때
    for j in range(N-i):
        for k in range(M-i):
            # arr[j][k] 는 정사각형 가장 왼쪽 위
            # 보고있는 정사각형의 꼭지점 숫자들이 전부 같을 때
            if arr[j][k] == arr[j][k+i] == arr[j+i][k+i] == arr[j+i][k]:
                print((i+1)**2) # 넓이 구해서 출력
                exit() # 코드 종료