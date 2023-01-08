import sys
sys.stdin=open('input.txt')

T= int(input())
for tc in range(T):
    x1, y1 , x2, y2 = map(int, input().split())
    n = int(input())
    totals = list(list(map(int, input().split())) for _ in range(n))
    # print(totals)
    count = 0
    for i in totals:
        # print(i)
        if i[0]- i[2] <= x1 <= i[0]+i[2] or i[0]- i[2] <= x2 <= i[0]+i[2]:
            if i[1]- i[2] <= y1 <= i[1]+i[2] or i[1] - i[2] <= y2 <= i[1]+i[2]:
                if x1 == i[0]- i[2] or x1 == i[0]+i[2]:
                    if i[1]- i[2] == y1 or y1 == i[1]+i[2]:
                        pass
                elif i[0] - i[2] == x2 or x2== i[0]+i[2]:
                    if i[1]- i[2] == y2 or y2== i[1]+i[2]:
                        pass
                else:
                    count+=1
    print(count)
