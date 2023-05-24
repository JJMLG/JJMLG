from collections import deque

def check(lst):
    pair = { ')': '(', '}': '{', ']': '[' }     # 짝이 맞는지 확인하기 위한 dict
    stk = []                                    # 여는 괄호만 담을 스택
    for s in lst:
        if s in '({[':                          # 여는 괄호는 추가
            stk.append(s)
        elif not stk or stk[-1] != pair[s]:     # 닫는 괄호인데 빈스택이면 False
            return False                        # 닫는 괄호인데 짝이 안맞으면 False
        else:                       # 닫는 괄호인데 짝이 맞으면 맞는 짝 빼준다
            stk.pop()
    return len(stk) == 0            # 비어 있어야 모두 짝을 찾은 것.


def solution(s):
    ans = 0
    Q = deque(list(s))              # 맨 앞에서 빼고 맨 뒤에 넣으니까 deque 활용
    for _ in range(len(s)):         # 길이만큼 해준다
        Q.append(Q.popleft())       # 빼고, 넣고
        if check(list(Q)):          # 올바른지 확인
            ans += 1
    return ans
