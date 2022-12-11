N = int(input())
start, end = input().split('*')
for n in range(N):
    file = input()
    if len(start) + len(end) > len(file): print('NE')
    else: print('DA' if start == file[:len(start)] and end == file[-len(end):] else 'NE')

"""
abc*def
와 같은 경우가 테스트케이스에 포함되어 있음
"""