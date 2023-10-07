n = int(input())
numbers = list(map(int,input().split()))
plus,minus,multiple,division = map(int,input().split())
result = []
def dfs(num,p,mi,mul,div,idx):
    if idx == n:
        result.append(num)
        return
    # print(num)
    if p > 0:
        dfs(num + numbers[idx], p-1,mi,mul,div,idx+1)
    if mi > 0:
        dfs(num - numbers[idx], p,mi-1,mul,div,idx+1)
    if mul > 0:
        dfs(num * numbers[idx], p,mi,mul-1,div,idx+1)
    if div > 0:
        dfs(int(num/numbers[idx]), p,mi,mul,div-1,idx+1)
    
    


dfs(numbers[0],plus,minus,multiple,division,1)
print(max(result))
print(min(result))