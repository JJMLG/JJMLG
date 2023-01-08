import sys

input = sys.stdin.readline

stack = []
result = 0
for _ in [0]*int(input().rstrip()):
    height = int(input().rstrip())
    while stack and height>=stack[-1]: stack.pop() # 스택안의, 높이가 낮은 건물들 전부 삭제
    result += len(stack) # while문을 통과하고 스택에 남아있는 건물들은, 현재 건물의 옥상을 볼 수 있다
    stack.append(height) # 현재 건물 추가
print(result)

# https://www.acmicpc.net/problem/6198