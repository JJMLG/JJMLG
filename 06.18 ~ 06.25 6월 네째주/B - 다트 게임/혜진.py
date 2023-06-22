def solution(dartResult):
    i = 0
    arr = []
    while i < len(dartResult):
        if dartResult[i] == '*':
            i += 1
            if len(arr) == 0: continue
            arr[-1] *= 2
            if len(arr) > 1:
                arr[-2] *= 2
        elif dartResult[i] == '#':
            i += 1
            if len(arr) == 0: continue
            arr[-1] *= -1
        else:
            if dartResult[i + 1] == '0':
                n = 10
                i += 3
            else:
                n = int(dartResult[i])
                i += 2
            if dartResult[i - 1] == 'D':
                n **= 2
            elif dartResult[i - 1] == 'T':
                n **= 3
            arr.append(n)
            
    return sum(arr)
