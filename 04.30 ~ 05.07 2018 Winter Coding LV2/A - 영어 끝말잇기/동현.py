def solution(n, words):
    answer = []

    wordList = []
    
    for i in range(len(words)):
        if words[i] in wordList:
            answer.append((i % n) + 1)
            answer.append((i//n) + 1)
            break
        if wordList and words[i][0] != wordList[-1][-1]:
            answer.append((i % n) + 1)
            answer.append((i//n) + 1)
            break
        wordList.append(words[i])
    
    if answer == []:
        return [0,0]
        
        

    return answer