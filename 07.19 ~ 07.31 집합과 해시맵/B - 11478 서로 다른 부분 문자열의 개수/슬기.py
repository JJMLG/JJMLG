import sys
sys.stdin = open('input.txt')

s = input()
ans = set()
#
# for i in range(len(s)):
#     for j in range(i, len(s)):
#         ans.add(s[i:j+1])
# print(len(ans))


idx = 0
flag = 1

while flag + idx <= len(s):
    ans.add(s[idx:idx + flag])
    if idx + flag >= len(s):
        flag += 1
        idx = 0
    else:
        idx += 1
print(len(ans))