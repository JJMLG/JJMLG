from collections import defaultdict


def solution(book_time):
    answer = 0

    book_time.sort()

    db = defaultdict(int)

    for start, end in book_time:
        start = start.split(":")
        end = end.split(":")
        start_time = int(start[0]) * 60 + int(start[1])
        end_time = int(end[0]) * 60 + int(end[1])

        # 퇴실 시간 확인
        for room in db.keys():
            if db[room] <= start_time:
                db[room] = end_time + 10
                break
        else:
            db[answer] = end_time + 10
            answer += 1

    return answer