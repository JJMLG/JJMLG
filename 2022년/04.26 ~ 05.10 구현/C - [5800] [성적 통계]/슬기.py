import sys
sys.stdin = open('input.txt')

k = int(input())



for i in range(k):
    student = list(map(int, input().split()))
    # print(student)
    maxx = max(student[1:])
    minn = min(student[1:])
    gap = sorted(student[1:], reverse=True)

    biggap = []
    for j in range(len(gap)-1):
        # print(j)
        biggap.append(gap[j] - gap[j+1])
    # print(biggap)
    largegap = max(biggap)
    # print(largegap)
    # print(gap)
    print('Class ' + str(i+1))
    print('Max ' + str(maxx) + ',', 'Min ' + str(minn) + ',', 'Largest gap ' + str(largegap))
