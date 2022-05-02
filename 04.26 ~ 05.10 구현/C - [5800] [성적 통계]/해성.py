K=int(input())
schoolClass = [list(map(int, input().split())) for _ in range(K)]
# print(schoolClass)

for indexx in range(1,K+1):
    largests = 0
    classList = schoolClass[indexx-1][1:]
    sortedClass = sorted(classList)
    for i in range(len(sortedClass)-1):
        if largests < sortedClass[i+1] - sortedClass[i]:
            largests = sortedClass[i+1] - sortedClass[i]
    print("Class " + str(indexx))
    print("Max " + str(max(classList)) + ',', "Min " + str(min(classList)) +',', "Largest gap " + str(largests))