import sys
sys.stdin = open('input.txt')

car = int(input())
start = {}
leave = []

cnt = 0

for i in range(car):
    car_number = input()
    start[car_number] = i

for _ in range(car):
    car_number = input()
    leave.append(car_number)

for x in range(car-1):
    for y in range(x+1, car):
        # print(start[leave[x]], start[leave[y]])
        if start[leave[x]] > start[leave[y]]:
            cnt += 1
            break

print(cnt)