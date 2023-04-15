def solution(players, callings):

    play = {}
    rank = {}

    for i in range(len(players)):
        if players[i] not in play:
            play[players[i]] = i

    for i in range(len(players)):
        if i not in rank:
            rank[i] = players[i]

    for i in callings:
        now = play[i]
        fast = now - 1
        front = rank[fast]

        rank[now] = front
        rank[fast] = i

        play[i] = fast
        play[front] = now

    return list(rank.values())