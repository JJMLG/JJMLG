N = int(input())
K = int(input())
picks = list(map(int, input().split())) # 추천 후보

result = []

# [후보번호, 추천수, 등록시간]
for i in range(K):
    # print(result)
    if len(result) < N: # 사진틀이 남았을 때
        # 이미 있는 후보를 추천하는지 확인
        in_result = False
        idx = 0
        for k in range(len(result)):
            if picks[i] == result[k][0]:
                in_result = True
                idx = k

        if not in_result: # 이미 있는 후보가 아닐 경우
            result.append([picks[i], 1, i]) # 후보 추가
        else: # 있는 후보일 경우
            result[idx][1] += 1 # 추천 +1
    
    else: # 사진틀이 남지 않았을 때
        # 이미 있는 후보를 추천하는지 확인
        in_result = False
        idx = 0
        for k in range(N):
            if picks[i] == result[k][0]:
                in_result = True
                idx = k

        if not in_result: # 이미 있는 후보가 아닐 경우
            # 후보 사진을 갈아끼워야 함
            recommended = 10**3 # 가상의 추천수 최대값
            recommend_idx = 0 # 가장 추천을 많이 받은 후보의 인덱스
            oldest_time = 10**3 # 가상의 등록순서 최대값
            oldest_idx = 0 # 가장 오래전에 등록된 후보의 인덱스
            for j in range(N): # 후보 사진들 중
                # 추천이 가장 적은 후보 찾기
                if result[j][1] < recommended:
                    recommended = result[j][1]
                    recommend_idx = j
                    # 동시에 그 후보의 등록시간도 기록
                    oldest_time = result[j][2]
                    oldest_idx = j

                # 추천수가 가장 적은 후보가 여러명일 때
                elif result[j][1] == recommended:
                    # 등록시간이 오래된 후보를 찾아서
                    if oldest_time > result[j][2]:
                        oldest_time = result[j][2]
                        oldest_idx = j
                        recommend_idx = oldest_idx # 인덱스 잡고
            # print(recommend_idx)
            result[recommend_idx] = [picks[i], 1, i] # 덮어씌우기
        else: # 있는 후보일 경우
            result[idx][1] += 1 # 추천 +1
    # print(result)

result.sort(key=lambda x:x[0]) # 후보번호순 정렬
for r in result:
    print(r[0], end=' ') # 출력