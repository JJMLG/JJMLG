import sys
sys.stdin = open('input.txt')

new_word = []

s = input()
# print(s)

for i in range(len(s)):
    new_word.append(s[i::])

order_word = sorted(new_word, key=lambda x: str(x))

for j in order_word:
    print(j)