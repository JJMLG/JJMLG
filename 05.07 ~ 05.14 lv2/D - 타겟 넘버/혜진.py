ans = 0

def solution(numbers, target):
    def DFS(cur, v, L, target):
        global ans
        if cur == L:
            if v == target:
                ans += 1
            return
        DFS(cur + 1, v + numbers[cur], L, target)
        DFS(cur + 1, v - numbers[cur], L, target)

    DFS(1, numbers[0], len(numbers), target)
    DFS(1, -numbers[0], len(numbers), target)
    return ans
