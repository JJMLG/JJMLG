import sys
sys.stdin = open('input.txt')

attendance = int(input())

stay = {}
cnt = 0
for i in range(attendance):
    name, status = input().split()
    if status == 'enter':
        stay[name] = 1
    else:
        del(stay[name])

stay = sorted(stay.keys(), reverse=True)

for j in stay:
    print(j)