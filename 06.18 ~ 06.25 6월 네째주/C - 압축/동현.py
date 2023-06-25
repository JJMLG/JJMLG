def solution(msg):
    answer = []
    dic = {}
    for i in range(65,91):
        dic[chr(i)] = i-64

    result = []
    last = 27
    high = 0
    for i in range(len(msg)):
        if i < high: # 0
            continue
        temp = msg[i]

        while True:
            
            if temp in dic:
                high += 1
                if high >= len(msg):
                    break
                temp += msg[high]
            else:
                result.append(dic[temp[:len(temp)-1]])
                dic[temp] = last
                last += 1
                break

    result.append(dic[temp])

    return result