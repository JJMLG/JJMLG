def solution(n, arr1, arr2):
    answer = []
    map = []
    # print(map)

    for i in range(len(arr1)):
        first_map = format(arr1[i], 'b')
        # print(len(first_map))
        if len(first_map) < n:
            map.append('0' + first_map)
        else:
            map.append(first_map)
        # print(bin(arr1[i]))
        # 길이에 못 미치면 맨 앞에 0 추가 > 9가 1001인데 길이 5 아니라서 앞에 0 추가
    print(map)

    return answer

# 한 변 길이 n
# 두 지도에서 겹치는 벽은 벽, 겹치는 공백은 공백
