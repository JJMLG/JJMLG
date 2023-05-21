from heapq import heappop, heappush, heapify

def makeMin(lst):
    res = [0, 0]
    res[0] = 60 * int(lst[0][:2]) + int(lst[0][3:])
    res[1] = 60 * int(lst[1][:2]) + int(lst[1][3:]) + 10
    return res

def solution(book_time):
    for i in range(len(book_time)):
        book_time[i] = makeMin(book_time[i])
    book_time.sort()
    
    ans = 1
    hq = []
    for s, e in book_time:
        if not hq:
            heappush(hq, e)
        elif hq[0] <= s:
            heappop(hq)
            heappush(hq, e)
        else:
            ans += 1
            heappush(hq, e)

    return ans



def solution(book_time):
    timeArr = [0] * (60 * 24)

    for s, e in book_time:
        sMin = 60 * int(s[:2]) + int(s[3:])
        eMin = 60 * int(e[:2]) + int(e[3:]) + 10
        
        if eMin > 60 * 24 - 1:
            eMin = 60 * 24 - 1
            
        timeArr[sMin] += 1
        timeArr[eMin] -= 1
    
    ans = 0
    for t in range(1, 60 * 24):
        timeArr[t] += timeArr[t - 1]
        if ans < timeArr[t]:
            ans = timeArr[t]
    
    return ans
