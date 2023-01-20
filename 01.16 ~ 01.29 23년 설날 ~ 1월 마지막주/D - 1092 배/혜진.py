# 내림차순 정렬
N = int(input())
cranes = sorted(list(map(int, input().split())), reverse=True)
M = int(input())
boxes = sorted(list(map(int, input().split())), reverse=True)

# 가장 큰 박스를 옮길 수 없으면 바로 종료
if cranes[0] < boxes[0]:
    print(-1)
    exit()

# 옮긴 박스는 .pop(idx)
t = 0
while boxes:
    for crane in cranes:
        for b in range(len(boxes)):
            # 옮겼으면 다음 크레인으로 넘어가야함 -> break
            if crane >= boxes[b]:
                boxes.pop(b)
                break
    # 크레인 한바퀴 다 돌았으면 1분 지남
    t += 1

print(t)