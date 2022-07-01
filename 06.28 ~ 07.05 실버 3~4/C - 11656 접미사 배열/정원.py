"""
접미사를 모아서, 정렬 후 출력
"""
word = input()
arr = []
for i in range(len(word)): arr.append(word[i:len(word)])
arr.sort()
for a in arr: print(a)