from collections import deque
def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    summ = sum(queue1) + sum(queue2)
    
    sumQueue1 = sum(queue1)
    sumQueue2 = sum(queue2)
    target = summ / 2
    cnt1, cnt2 = 0, 0
    end = len(queue1) * 2
    if summ % 2 == 1:
        return -1
    else:
        while cnt1 <= end and cnt2 <= end:
        
            if sumQueue1 > target:
                tmp = queue1.popleft()
                queue2.append(tmp)
                answer += 1
                cnt1 += 1
                sumQueue1 -= tmp
                sumQueue2 += tmp
            elif sumQueue2 > target:
                tmp = queue2.popleft()
                queue1.append(tmp)
                answer += 1
                cnt2 += 1
                sumQueue1 += tmp
                sumQueue2 -= tmp
            else:
                return cnt1 + cnt2
            


        return -1