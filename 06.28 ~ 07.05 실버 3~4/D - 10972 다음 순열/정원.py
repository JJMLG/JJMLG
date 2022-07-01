"""
흑흑...😭 두 시간 박치기 하고 도저히 안되서 답지 봄 ㅠㅠ
"""
N = int(input())
M = list(map(int, input().split()))
find = False
"""
ex) 1 2 3 5 4
1. 뒤에서부터 숫자 두개씩 비교하다가
2. 뒤에 숫자(5)가 앞에 숫자(3)보다 클 때
3. 다시 맨 뒤에서부터 시작하여
4. 2에서 비교하여 더 작았던 앞에 숫자(3)보다 큰 수(4)를 찾으면
5. 둘(3, 4)의 자리를 바꿔줌 (1 2 3 5 4 -> 1 2 4 5 3)
6. 찾았던 앞의 숫자보다 큰 수(4)의 뒤쪽을 오름차순 정렬
7. 앞부분과 정렬된 뒷부분을 붙여서 출력
"""
for i in range(N-1, 0, -1):
    if M[i-1] < M[i]:
        for j in range(N-1, 0, -1):
            if M[i-1] < M[j]:
                M[i-1], M[j] = M[j], M[i-1]
                M = M[:i] + sorted(M[i:])
                find = True
                break
    if find:
        print(*M)
        break
if not find:
    print(-1)