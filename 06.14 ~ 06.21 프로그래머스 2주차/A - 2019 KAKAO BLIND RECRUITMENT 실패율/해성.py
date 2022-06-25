def solution(N, stages):
    answer = []
    totalPeopleCount = len(stages)
    failRecord = [[0, i] for i in range(N + 2)]
    stages = sorted(stages)
    eachStageFailCount = [0 for _ in range(N + 2)]
    PeopleCount = [0 for _ in range(N + 2)]

    #     스테이지별 실패 유저 수 기록
    for j in stages:
        eachStageFailCount[j] += 1
    #     도전인원 기록
    failPeople = totalPeopleCount
    for i in range(1, len(eachStageFailCount)):
        failPeople -= eachStageFailCount[i - 1]
        PeopleCount[i] = failPeople
        if failPeople == 0:
            break
    for j in range(1, len(eachStageFailCount)):
        if eachStageFailCount[j] == 0:
            pass
        else:
            failRecord[j][0] = eachStageFailCount[j] / PeopleCount[j]
    failRecord = failRecord[1:len(eachStageFailCount) - 1]
    for i in range(len(failRecord) - 1):
        for j in range(len(failRecord) - i - 1):
            if failRecord[j][0] < failRecord[j + 1][0]:
                failRecord[j], failRecord[j + 1] = failRecord[j + 1], failRecord[j]
            else:
                pass
    for i in failRecord:
        answer.append(i[1])
    return answer