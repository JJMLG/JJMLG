def solution(id_list, report, k):
    answer = [0] * len(id_list) # 정답 배열
    report_list = [[] for _ in range(len(id_list))] # 신고받은 목록
    black_list = [0] * len(id_list) # 신고받은 횟수
    for r in report:
        user, reported = r.split() # 공백을 간격으로, 유저, 피신고자
        if reported not in report_list[id_list.index(user)]: # 중복 신고 방지, 아직 신고 받은 적 없는지 확인
            report_list[id_list.index(user)].append(reported) # 신고 받은 목록 추가
            black_list[id_list.index(reported)] += 1 # 신고 받은 횟수 추가
    # print(id_list, report, k) # 디버깅
    # print(report_list, black_list) # 디버깅
    for i in range(len(id_list)): # 해당 유저가
        for a in report_list[i]: # 신고한 사람이
            if black_list[id_list.index(a)] >= k: # k번 이상 신고 되었을 때
                answer[i] += 1 # 제재완료
    return answer