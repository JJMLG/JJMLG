def solution(lottos, win_nums):
    answer = []
    # print(lottos, win_nums)
    # 일치하는 번호의 개수만이, 오직 등수에 영향을 줌
    minn = 0
    for l in lottos:
        if l in win_nums:
            minn += 1
    result = [6, 6, 5, 4, 3, 2, 1] # 등수 테이블
    answer.append(result[lottos.count(0)+minn])
    answer.append(result[minn])    
    return answer