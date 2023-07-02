# def solution(cacheSize, cities):
#     if cacheSize == 0:
#         return 5 * len(cities)
#     lru = []
#     ans = 0
#     for i in range(len(cities)):
#         city = cities[i].lower()
#         if city in lru:
#             lru.remove(city)
#             ans += 1
#         elif len(lru) == cacheSize:
#             lru.pop(0)
#             ans += 5
#         else:
#             ans += 5
#         lru.append(city)
#     return ans


from collections import deque

def solution(cacheSize, cities):
    ans = 0
    lru = deque([], cacheSize)
    for c in cities:
        c = c.lower()
        if c in lru:
            lru.remove(c)
            lru.append(c)
            ans += 1
        else:
            lru.append(c)
            ans += 5
    return ans
