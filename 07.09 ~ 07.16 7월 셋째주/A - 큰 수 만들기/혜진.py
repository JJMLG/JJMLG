# 시간초과
# def solution(number, k):
#     l = len(number) - k
#     ans = number[:l]
    
#     def recur(st, si):
#         nonlocal ans
#         if len(st) == len(ans):
#             ans = st
#             return
#         for i in range(si, len(number)):
#             temp = st + number[i]
#             if int(ans[:len(temp)]) <= int(temp):
#                 recur(temp, i + 1)
    
#     recur('', 0)
#     return ans


# 스택
def solution(number, k):
    ans = []                # 결과
    for n in number:
        while ans and ans[-1] < n and k > 0:    # ans가 있고
            ans.pop()                           # 마지막 숫자가 지금 숫자(n)보다 작고
            k -= 1                              # 아직 제외 가능하면
        ans.append(n)       # n 넣기
    
    if k:                   # 더 빼야 하면
        ans = ans[:-k]      # 그만큼 더 빼기
    return ''.join(ans)
