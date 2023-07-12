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
    ans = []
    for n in number:
        while ans and ans[-1] < n and k > 0:
            ans.pop()
            k -= 1
        ans.append(n)
    
    if k:
        ans = ans[:-k]
    return ''.join(ans)
