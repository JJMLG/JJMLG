for t in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    result = 0
    for n in range(int(input())): # 각 행성을 입력
        cx, cy, cr = map(int, input().split())
        d1 = (x1-cx)**2 + (y1-cy)**2 # 출발점과 행성 중심간의 거리
        d2 = (x2-cx)**2 + (y2-cy)**2 # 도착점과 행성 중심간의 거리
        d3 = cr**2 # 행성 반지름의 제곱
        if d3 > d1 and d3 > d2: # 같은 행성 안에 있으면
            pass # 행성 진입/이탈할 필요 없음
            """
            위의 if문을 거치면서 아래 세가지 경우만 남게됨
            1. 출발점 도착점 다 행성 밖에 있는 경우, 진입/이탈 없이 행성 사이를 움직일 수 있음
            2. 출발점은 행성 안에, 도착점은 행성 밖에 있는 경우, 진입/이탈이 필요함
            3. 출발점은 행성 밖에, 도착점은 행성 안에 있는 경우, 진입/이탈이 필요함
            """
        elif d3 > d1: # Case 2
            result += 1
        elif d3 > d2: # Case 3
            result += 1
    print(result)