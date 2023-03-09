N = int(input())
M = int(input())
S = input()

idx = ans = 0
cnt = 0                         # IOI가 연속으로 나오는 갯수 => N과 비교한다
while idx < M - 1:
    if S[idx:idx+3] == 'IOI':
        cnt += 1
        idx += 2
        if cnt == N:
            ans += 1
            cnt -= 1
    else:
        idx += 1
        cnt = 0

print(ans)

'''
2중 반복문은 안된다
'''
