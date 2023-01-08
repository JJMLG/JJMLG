case = 1 # 테스트 케이스
while True:
    N = int(input()) # 사람 수
    if N == 0: break # while 종료
    result = [] # 결과를 담을 배열
    for n in range(N):
        A, B = input().split() # 사람 A, 사람 B
        flag = False # 이미 있는 그룹인지 확인할 것
        for i in range(len(result)): # 마니또 그룹들 중에서
            if A in result[i] or B in result[i]: # 둘 중 하나라도 속하는 그룹이 있다면
                flag = True # 둘 다 결국 같은 그룹
                # set()로 중복처리하면서 사람들을 다 추가할 것
                result[i].add(A)
                result[i].add(B)
        if not flag: # 둘 다 속한 마니또그룹이 없으면
            result.append(set()) # 그룹 추가
            # 사람들 추가
            result[-1].add(A)
            result[-1].add(B)
    print(case, len(result)) # 출력
    case += 1 # 다음 케이스