words = input()
sum = 0
result = set()
lens=len(words)
temp_word = ''
for i in range(lens):
    temp_word = ''
    for j in range(i, lens):
        temp_word+=words[j]
        if temp_word in result:
            pass
        else:
            result.add(temp_word)
print(len(result))

# for i in range(1,len(words)+1):
#     for j in range(len(words)-i+1):
#         if words[j:j+i] in result:
#             pass
#         else:
#             result.append(words[j:j+i])
#             sum+=1
# print(len(result))
# print(sum)
