import sys
sys.stdin= open('input.txt')
n,m = map(int,input().split())
arr = [list(input()) for _ in range(n)]

cntUp = 0
cntDown = 0
cntRight = 0
cntLeft = 0
for i in range(1,n):
    tmp_1 = 0 
    tmp_2 = 0
    for j in range(1,m):

        if arr[i][j] == '.' and arr[i-1][j] == 'X':
            tmp_1 += 1
        else:
            cntUp += tmp_1 //2
            tmp_1 = 0

        
        if arr[i][j] == '.' and arr[i+1][j] == 'X':
            tmp_2 += 1
        else:
            cntDown += tmp_2 // 2
            tmp_2 = 0
        

for j in range(1,m):
    tmp_3 = 0 
    tmp_4 = 0
    for i in range(1,n):

        if arr[i][j] == '.' and arr[i][j-1] == 'X':
            tmp_3 += 1
        else:
            cntLeft += tmp_3 //2
            tmp_3 = 0

        
        if arr[i][j] == '.' and arr[i][j+1] == 'X':
            tmp_4 += 1
        else:
            cntRight += tmp_4 // 2
            tmp_4 = 0

print(sum([cntUp,cntDown,cntLeft,cntRight]))