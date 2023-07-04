def solution(numbers):
    ans = []
    for num in numbers:
        if num % 2 == 0:            # 짝수면 이진수의 젤 오른쪽을 1로 한게 정답
            ans.append(num + 1)     # +1 한 수가 정답
            continue

        bi = '0' + bin(num)[2:]     # 홀수면 이진수로 만들고 앞에 0 붙이기
        idx = bi.rfind('0')         # 오른쪽부터 가장 처음 0인 index 찾기
        
        bi = list(bi)       # 문자열은 idx로 값을 못 바꾸니까
        bi[idx] = '1'       # 0을 1로
        bi[idx + 1] = '0'   # 다음이 1이면 0으로 하는게 더 작은 수
        ans.append(int(''.join(bi), 2))

    return ans
