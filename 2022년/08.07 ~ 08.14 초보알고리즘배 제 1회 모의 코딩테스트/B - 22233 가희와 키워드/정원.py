import sys

input = sys.stdin.readline

N, M = map(int, input().split())
K = set(input().rstrip() for _ in range(N)) # keyword
for _ in range(M): 
    tmp = set(input().rstrip().split(',')) # 개행문자('\n') 제거
    K -= tmp
    print(len(K))

"""
시간 : 21분
풀이
    시간은 1.5초지만 메모리가 넉넉한 문제이다
    제출언어로 PyPy를 사용한다
    빠른 입력을 위해 
    input = sys.stdin.readline도 사용한다
    N과 M은 둘 다 200,000으로 큰 편이다
    set 클래스인 A와 B에 대해서 A-B가 가능하다
    키워드를 담은 set(K)에서
    가희가 메모로 작성하여 없앤 키워드를 빼주고
    매번 글을 쓰고 남은 키워드 개수를 출력한다
"""