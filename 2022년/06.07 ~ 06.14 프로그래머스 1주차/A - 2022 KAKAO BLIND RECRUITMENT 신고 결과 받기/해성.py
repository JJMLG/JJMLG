def solution(id_list, report, k):
    # 1. 신고한 거 모두 기록(중복 신고 제거)
    # 2. 신고한 것 중 k개 이상이면 제거해야할 사람들이므로 기록
    # 3. 1번의 기록에서 신고자의 value값이 2번의 신고대상자에 포함되면 그 숫만큼 답으로

    #     얼마나 신고되었는지 기록숫자
    reportedCount = dict()

    #     말그대로 아이디당 리포트 기록
    reportRecord = dict()

    #     받을 결과 메일 수
    answer = [0] * len(id_list)

    #     각 아이디별로 신고한 사람 명단 기록하기 위해 reportRecord에 value 값으로 빈 배열 초기화
    #     각 아이디에 신고받은 수 기록할 reportedCount 0으로 초기화
    for id in id_list:
        reportRecord[id] = []
        reportedCount[id] = 0
    # print(reportRecord,"reportRecord")
    # print(reportedCount,"reportcount")
    #
    #   report 배열에서 띄어쓰기를 기준으로 앞 reporter는 신고한사람, badperson는 신고당한 사람
    for eachReport in report:
        reporter, badPerson = eachReport.split(' ')
        #         신고한 사람의 value 값이 없으면 밑 count메서드 오류가 나므로
        # if reportRecord[reporter]!=False:
        #         이미 그사람을 해당 신고자가 한번신고 했으면 pass 안했으면 배열에 추가
        if reportRecord[reporter].count(badPerson):
            pass
        else:
            reportRecord[reporter].append(badPerson)
    #     신고된 사람들 명단 reportedMembers만 다시 기록
    # 2.
    reportedMembers = []
    # print(reportRecord, "요기")
    #     신고 기록에서 신고된 사람들값
    for eachReportedList in reportRecord.values():
        for eachReportedPerson in eachReportedList:
            reportedCount[eachReportedPerson] += 1
            if reportedCount[eachReportedPerson] >= k:
                reportedMembers.append(eachReportedPerson)
    if len(reportedMembers) == False:
        return answer
    else:
        for idx in range(len(id_list)):
            # print(reportRecord)
            tempCount = 0
            for j in reportRecord[id_list[idx]]:
                if j in reportedMembers:
                    tempCount += 1
            answer[idx]= tempCount
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))