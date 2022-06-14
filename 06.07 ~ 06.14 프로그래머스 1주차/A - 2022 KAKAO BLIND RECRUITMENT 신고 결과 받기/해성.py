def solution(id_list, report, k):
    #     얼마나 신고되었는지 기록숫자
    reportCount = dict()
    #     말그대로 아이디당 리포트 기록
    record = dict()
    #     받을 결과 메일 수
    answer = []
    for i in id_list:
        record[i] = []
        reportCount[i] = 0

    for i in report:
        a, b = i.split(' ')
        if record[a] != False:
            if record[a].count(b):
                pass
            else:
                record[a].append(b)

    reportedMembers = []
    for i in record.values():
        for j in i:
            reportCount[j] += 1
            if reportCount[j] >= k:
                reportedMembers.append(j)
    if len(reportedMembers) == False:
        answer = [0] * len(id_list)
    else:
        for id in id_list:
            # print(record)
            tempCount = 0
            for j in record[id]:
                if j in reportedMembers:
                    tempCount += 1
            answer.append(tempCount)
    return answer