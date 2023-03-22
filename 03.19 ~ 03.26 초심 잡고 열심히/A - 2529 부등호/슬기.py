import sys
sys.stdin = open('input.txt')

k = int(input())
inequality = input().split(' ')

visited = [0] * 10
max_ans = ''
min_ans = ''

def check(x, y, z):     # 왼쪽 숫자, 오른쪽 숫자, 부등호
    if z == '<':
        return x < y
    else:
        return x > y

def solve(depth, s):
    global max_ans, min_ans

    if depth == k+1:
        if len(min_ans) == 0:
            min_ans = s
        else:
            max_ans = s
        return

    for i in range(10):
        if visited[i] == 0:
            if depth == 0 or check(s[-1], str(i), inequality[depth-1]):
                visited[i] = 1
                solve(depth+1, s+str(i))
                visited[i] = 0
solve(0, '')
print(max_ans)
print(min_ans)