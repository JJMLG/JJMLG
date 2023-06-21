dic = {}                        # 했던 숫자 반복을 없애기 위함
def convert(n, base):
    try:
        return dic[n]           # 아는 숫자는 그대로 return
    except:
        T = '0123456789ABCDEF'
        q, r = divmod(n, base)
        dic[n] = convert(q, base) + T[r] if q else T[r]
        return dic[n]           # 모르는 숫자는 찾아서 return

def solution(n, t, m, p):
    temp = ans = ''
    num = 0                     # 바꿔줄 숫자
    while len(temp) < m * t:    # m명이 t개를 말하니까 m * t
        temp += convert(num, n)
        num += 1
    # print(temp)
    for i in range(p - 1, m * t, m):    # p - 1번째 인덱스부터 m 간격으로
        ans += temp[i]
    return ans
