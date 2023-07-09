from collections import deque
def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5*len(cities)
    answer = 0
    queue = deque()
    for city in cities:
        city = city.lower()

        if city not in queue:
            if queue and len(queue) >= cacheSize:
                queue.popleft()
            queue.append(city)
            
            answer += 5
        else:
            queue.remove(city)
            queue.append(city)
            answer += 1
                
    return answer