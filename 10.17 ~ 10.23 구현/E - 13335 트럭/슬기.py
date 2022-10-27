import sys
sys.stdin = open('input.txt')

truck, bridge, weight_limit = map(int, input().split())
t_weight = list(map(int, input().split()))

visited = [0] * bridge
now, time = 0, 0


while True:
    out = visited.pop(0)
    now -= out

    if t_weight:
        if now + t_weight[0] <= weight_limit:
            visited.append(t_weight[0])
            now += t_weight[0]
            t_weight.pop(0)
        else:
            visited.append(0)

    time += 1

    if not visited:
        break
print(time)