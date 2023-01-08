"""
어차피 맨뒤에 새로운 알파벳이 추가된다
S에 추가하는게 아닌 T에서 하나씩 빼자
break 경우만 잘 생각해주기
"""

S = input()
T = input()

while True:
    if S == T:
        print(1)
        break
    elif len(S) >= len(T):
        print(0)
        break

    T = T[:-1] if T[-1] == "A" else T[:-1][::-1]
