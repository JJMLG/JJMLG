"""
일렬로 줄을 세우는 경우는 총 n!
result에 담기는 맨 처음 수는 k // (n - 1) + 1
처음 수가 담기면, 일렬로 다시 세우는 경우를 반복. 이때 n은 n - 1, k는 k % (n - 1)!
"""

def facto(n):
    if n < 1:
        return 1
    else:
        # print(n)
        return n * facto(n - 1)


def solution(n, k):
    answer = []

    arr = list(range(1, n + 1))

    while n != 0:
        num_case = facto(n - 1)
        # print(num_case)
        idx = k // num_case
        k = k % num_case
        if k == 0:
            answer.append(arr.pop(idx - 1))
        else:
            answer.append(arr.pop(idx))
        n -= 1

    return answer


"""
def solution(n, k):
    answer = []
    visited = [0 for _ in range(n)]

    cnt = 0
    tmp = []
    def recur(cur):
        nonlocal cnt, tmp
        if cur == n:
            cnt += 1
            if cnt == k:
                # print(cnt, '?')
                tmp = answer[:]
                # print(tmp)
            # print(answer)
            return
        
        for i in range(1, n + 1):
            if visited[i-1]:
                continue
            visited[i-1] = True
            answer.append(i)
            recur(cur+1)
            answer.pop()
            visited[i-1] = False
            
        
    recur(0)
    # recur(0, 0)
    
    return tmp
"""