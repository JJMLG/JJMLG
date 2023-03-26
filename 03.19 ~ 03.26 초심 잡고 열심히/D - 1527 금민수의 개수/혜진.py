from itertools import product                       # 중복 있는 순열

A, B = map(int, input().split())
cnt = 0

for n in range(len(str(A)), len(str(B)) + 1):       # 숫자의 길이 범위
    for nums in product(['4', '7'], repeat=n):      # ['4', '7']에서 중복 가능하게 n개를 뽑는다
        tmp = int(''.join(list(nums)))
        if A <= tmp <= B:
            cnt += 1

print(cnt)
