N = int(input())
result = 0 # 그룹단어개수 초기화
for n in range(N):
    word = input()
    char = [] # 사용한 글자
    for i in range(len(word)): # 단어를 순회하면서
        if word[i] not in char: # 사용한 적 없는 글자라면
            char.append(word[i]) # 사용한 글자에 추가
        else: # 사용한 적 있는 글자라면
            if word[i] != word[i-1]: # 앞글자와 다르다면
                result -= 1 # 그룹단어가 아닙니다
                # 매 케이스 그룹단어라고 가정하고
                # 그룹단어가 아닐 경우 -1 하였음
                break
    result += 1 # 그룹단어입니다!
print(result) # 출력