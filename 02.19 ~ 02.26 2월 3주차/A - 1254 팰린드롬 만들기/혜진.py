def ispal(s):
    L = len(s)
    for i in range(L//2):
        if s[i] != s[L - 1 - i]:
            return False
    return True

s = input()
_s = ''

if ispal(s):
    print(len(s))
    exit()

for c in s:
    _s = c + _s
    if ispal(s + _s):
        break

print(len(s + _s))