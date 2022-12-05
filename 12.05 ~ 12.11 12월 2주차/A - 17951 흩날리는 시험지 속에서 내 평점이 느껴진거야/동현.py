import sys
sys.stdin = open('input.txt')

n, k = map(int,input().split())
ls = list(map(int,input().split()))


start = 0 
end = n-1
mid = (start+end) // 2
minn = min(sum(ls[0:mid]),sum(ls[mid:n]))
print(minn)
while start <= end:
    mid = (start+end) // 2
    print(ls[0:mid])
    print(ls[mid:n])
    break
