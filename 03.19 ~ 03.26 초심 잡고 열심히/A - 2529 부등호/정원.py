K = int(input())
sign = input().split()
visited = [0]*10 # 0~9
maxx, minn = "", ""

def check(a, b, K):
    # 1<2 : True
    # '1'<'2' : True
    if K == '<':
        return a<b # T or F
    if K == '>':
        return a>b # T or F

def recur(idx, num):
    global maxx, minn

    if idx == K+1:
        if not minn: # 가장 먼저 부등호를 완성한 숫자가 최소값
            minn = num
        else: # 최소값을 찾았을 경우, 이후 나오는 숫자들로 최대값 갱신
            maxx = num
        return # 아래 for문 스킵
    
    for i in range(10):# 0부터 9까지 
        if not visited[i]:
            # 디버깅
            # if idx != 0:
            #     print(*list(num))
            #     print('', *sign[:len(num)-1])
            #     print(num[-1], sign[idx-1], i)
            #     print()
            if idx == 0 or check(num[-1], str(i), sign[idx-1]):
                visited[i] = 1 # visited 찍고
                recur(idx+1, num+str(i)) # 재귀
                visited[i] = 0 # visited 풀고

recur(0, "")
print(maxx)
print(minn)