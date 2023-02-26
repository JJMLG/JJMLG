S = input()
L, S_rev = len(S), S[::-1]
result = 0

for i in range(L, 0, -1):
    if S_rev[:i] == S_rev[:i][::-1]:
        result = i+(L-i)*2
        break

print(result)

"""
ex) abczzzz -> abc + zzzz + cba

L = 문자열 전체의 길이(abczzzz)
i = 뒤에서 가장 긴 팰린드롬의 길이(zzzz)
L-i = 문자열 전체에서 가장 긴 팰린드롬을 뺀 길이(abc)
result = (L-i) + i + (L-i)
"""