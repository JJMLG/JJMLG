People = len(stages)
    faillist = []
    for i in range(1, N + 1):
        faillist.append(stages.count(i) / People)
        if stages.count(i) / People > 0:
            People -= stages.count(i)