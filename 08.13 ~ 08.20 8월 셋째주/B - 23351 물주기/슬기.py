import sys
sys.stdin = open('input.txt')

n, k, a, b = list(map(int, input().split()))

plant = [k] * n
cnt = 0
while True:
    # 계속 물 적은 쪽에만 물 주기 위해 정렬
    plant.sort()
    if 0 in plant:
        break

    # 물 주기
    for i in range(a):
        plant[i] += b

    # 물 감소
    for i in range(n):
        plant[i] -= 1
    cnt += 1

print(cnt)

