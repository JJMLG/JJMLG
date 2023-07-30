"""
입력이 좀 특이함
말고는 간단한 dict 문제
"""
import sys

dic = {}        # 나무종류: 수
N = 0           # 전체 나무 수
while True:
    tree = sys.stdin.readline().rstrip()
    if not tree:
        break
    dic[tree] = dic.get(tree, 0) + 1
    N += 1

keyArr = sorted(dic.keys())      # key값 오름차순 정렬
for key in keyArr:
    n = dic[key] / N * 100       # 계산
    print('%s %.4f' %(key, n))   # 소수점 4자리까지 출력
