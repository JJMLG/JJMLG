S = list(input())
T = list(input())
result = 0
# S를 T로 만들지 않고, T를 S로 만든다
# 이유는 두 가지
# 1.pop()에서 인덱스 없이 사용하여 속도 향상
# 2.추가, 뒤집고 추가 -> 제거, 제거 후 뒤집기
#   후자는 둘 다 일단 제거하고 시작하므로 더 직관적임
while True:
    if S == T:
        result = 1 # S를 T로 만들 수 있다!
        break # 종료
    if T[-1] == 'A':
        T.pop() # A를 빼주고
        if not T: # 마지막 문자를 뺐다면
            break # 종료
    elif T[-1] == 'B':
        T.pop() # B를 빼주고
        if not T: # 마지막 문자를 뺐다면
            break # 종료
        T = T[::-1] # 뒤집고
print(result) # 결과 출력