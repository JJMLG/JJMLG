def solution(alp, cop, problems):
    maxAlp = maxCop = 0         # 목표
    for problem in problems:
        maxAlp = max(maxAlp, problem[0])
        maxCop = max(maxCop, problem[1])

    dp = [[30000] * (maxCop + 1) for _ in range(maxAlp + 1)]
    
    alp = min(alp, maxAlp)
    cop = min(cop, maxCop)
    dp[alp][cop] = 0
    
    for i in range(alp, maxAlp + 1):
        for j in range(cop, maxCop + 1):
            if i + 1 <= maxAlp:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            if j + 1 <= maxCop:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)
            
            for aReq, cReq, aRwd, cRwd, cost in problems:
                if aReq <= i and cReq <= j:
                    nextAlp = min(maxAlp, i + aRwd)
                    nextCop = min(maxCop, j + cRwd)
                    dp[nextAlp][nextCop] = min(dp[nextAlp][nextCop], dp[i][j] + cost)
    
    return dp[-1][-1]



# from heapq import heappush, heappop

# def solution(alp, cop, problems):
#     maxAlp = maxCop = 0
#     for problem in problems:
#         maxAlp = max(maxAlp, problem[0])
#         maxCop = max(maxCop, problem[1])
#     table = [[30000] * 151 for _ in range(151)]
#     problems += [[0, 0, 1, 0, 1], [0, 0, 0, 1, 1]]

#     hq = [(0, alp, cop)]
#     table[alp][cop] = 0
#     while hq:
#         currCost, currAlp, currCop = heappop(hq)
#         if currAlp >= maxAlp and currCop >= maxCop:
#             return currCost
        
#         if table[currAlp][currCop] <= currCost:
#             for reqAlp, reqCop, rwdAlp, rwdCop, cost in problems:
#                 nextAlp, nextCop = min(150, currAlp + rwdAlp), min(150, currCop + rwdCop)
#                 if currAlp >= reqAlp and currCop >= reqCop and currCost + cost < table[nextAlp][nextCop]:
#                     table[nextAlp][nextCop] = currCost + cost
#                     heappush(hq, (currCost + cost, nextAlp, nextCop))
