import sys
sys.stdin = open('input.txt')

"""
5를 높은 자리로 k 만날 때 까지m 세서 만나면 5000으로 바꿔주면서 가기 
m 으로 끝나면 다 1111로 변경
5를 낮은 자리수로 보내야 하므로 k 만나면 5로 바꾸기 (mk 묶으면 5가 높은 자리로 이동)
m이 연속 되면 묶어서 0 개수 늘리기
"""


word = input()

m = 0
tmp = ''
max_res = ''
min_res = ''
for i in word:
    tmp += i
    if i == 'M':
        m += 1
    else:   # k 일 때
        if m > 0:
            max_res += str((10 ** m) * 5)
            min_res += str((10**m) + 5)
        else:
            max_res += '5'
            min_res += '5'
        m = 0

if m > 0:
    max_res += '1' * m
    min_res += str(10**(m-1))

print(max_res)
print(min_res)