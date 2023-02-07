string = input()
L = len(string)

def ispal(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

if string == string[0] * L: # 같은 문자 반복이면 -1
    print(-1)
elif ispal(string):         # 팰린드롬이면 문자 하나 빼면 팰린드롬이 아님
    print(L - 1)
else:                       # 팰린드롬이 아니면 L
    print(L)
