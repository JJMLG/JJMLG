import sys

input = sys.stdin.readline

dct = dict() # tree dict
lst = [] # tree list
cnt = 0
while True:
    tree = input().rstrip() # EOFerror
    if not tree: break
    if tree not in lst: lst.append(tree)
    try: dct[tree] += 1
    except: dct[tree] = 1
    cnt += 1
lst.sort()
for l in lst: print(f'{l} {dct[l]/cnt*100:.4f}')

"""
rstrip을 통해 무제한 입력을 해결할 수 있음 (정답 제출 및 디버깅 시)
퍼센테이지 계산 시, 나무 종류 수가 아닌 나무 그루 수로 계산함에 주의
"""