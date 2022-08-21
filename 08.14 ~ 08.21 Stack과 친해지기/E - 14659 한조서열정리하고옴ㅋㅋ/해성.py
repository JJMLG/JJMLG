import sys
sys.stdin = open('input.txt')
N = int(input())
arr = list(map(int, input().split()))
result = []
maxx=0
cnt=0

for i in range(N):
    cnt =0
    for j in range(i+1,N):
        if arr[i] <= arr[j]:
            if maxx<cnt:
                maxx=cnt
            break
        else:
            cnt+=1
    if maxx<cnt:
        maxx=cnt
    # 남은게 maxx값과 같거나 작으면 어차피 그 뒤부터는 안봐도 됨.
    if N-i <= maxx:
        break
print(maxx)



