# import sys
N, M = map(int, input().split())
quad = [list(map(int, input())) for _ in range(N)]
minxx = min(N, M)
maxSize = 0
# 있으면 그거고
# 없으면 크기가 1이 젤 큰 사각형
# 두변중에 작은게 최대 정사각형 길이니까
for size in range(2, minxx+1):
    # 사각형 돌아보면서 체크
    for y in range(N):
        for x in range(M):
    # size안에서 길이 구하기 길이1은 볼 필요 없으니 1부터 더하기
            for width in range(1, size+1):
                # 꼭지점이 같으면
                if y+width <= N-1 and x+width <= M-1 and quad[y][x] == quad[y+width][x+width] == quad[y+width][x] == quad[y][x+width]:
                    if maxSize < (width+1)*(width+1):
                        maxSize = (width+1)*(width+1)
                else:
                    pass
if maxSize == 0:
    print(1)
else:
    print(maxSize)



