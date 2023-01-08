import sys


cnt = 0
n = int(input())
for i in range(n):
    wordlist = []
    word = input()
    for j in range(len(word)):
        if word[j] not in wordlist or word[j-1] == word[j]:
            wordlist.append(word[j])

        else:
            wordlist = []
            break

    if len(wordlist) == len(word):
        cnt += 1

print(cnt)