import sys
sys.stdin = open('input.txt')

n, p = map(int, input().split())

stack = [[] for _ in range(7)] # 1~6번 줄 까지 있음
cnt = 0
for i in range(n):
    mel_n, mel_p = map(int, input().split())

    if not stack[mel_n-1]:
        stack[mel_n-1].append(mel_p)
        cnt += 1
        # print(stack)
    else:
        while stack[mel_n-1] and mel_p < stack[mel_n-1][-1]:
            stack[mel_n-1].pop()
            cnt += 1
        if not stack[mel_n-1] or mel_p > stack[mel_n-1][-1]:
            stack[mel_n-1].append(mel_p)
            cnt += 1
        else:
            pass

print(cnt)