import sys



n,x,y = map(int,input().split())

ls = [0]*(2*n)
visited = [0]*(n+1)
result  = []
def dfs(depth,lst):
    
    # x와 y의 값이 다르면 필요없음
    if lst[x-1] != lst[y-1]:
        return
    
    # depth 가 2*n 이 되면 result에 추가하고 끝내야댐
    if depth == 2*n:
        result.append(lst[:])
        return

    if lst[depth] != 0:
        dfs(depth+1,lst)
    else:
        for i in range(1,n+1):
            
            # 이미 lst에 들어간 숫자라면 버림
            if visited[i] == 1:
                continue
            # 이미 depth 혹은 depth+i+1 자리가 차있다면 버림
            if depth+1+i >= 2*n  or lst[depth+i+1] != 0:
                continue
            lst[depth] = i
            lst[depth+i+1] = i 
            visited[i] = 1
            dfs(depth+1,lst)
            lst[depth] = 0
            lst[depth+i+1] = 0
            visited[i] = 0
        
    
dfs(0,ls)
print(len(result))