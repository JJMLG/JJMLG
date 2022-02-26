import sys
sys.stdin = open('14719.txt')

H, W = list(map(int,input().split()))
# print(H,W)
world = list(map(int,input().split()))
# print(world)
# 맨 처음 블록을 기준으로 그 다음부터 그 값보다 크거나 같은 값까지 기준 - 다음 값들
# 그리고 기준보다 크거나 같은값 나오면 그 값이 기준이됨
# 근데 기준보다 바로 그 담이 큰 값나오면 기준을 바꿈
# 그리고
end_value = 0
end_point = 0
start_value = 0
start_point = 0
STD_value = start_value
STD_point = start_point

for i in range(len(world)):
    if world[i] !=0:
        start_point = i
        start_value = world[i]
        break
    else:
        pass
# print(start_point)
# print(start_value)

result = 0
while end_point:
    for i in range(start_point, len(world)):
        # print(i)
        # i가 시작지점과 같지 않고 시작값보다 크다면
        if i > start_point and world[i] >= start_value:
            if i-start_point ==1:
                start_point = i
                start_value = world[i]
            else:
                end_point = i
                end_value = world[i]
                for i in world[start_point:end_point]:
                    result += start_value-world[i]
                start_value = end_value
                start_point = end_point
        elif i > start_point and world[i] < start_value:
            pass
print(result)






