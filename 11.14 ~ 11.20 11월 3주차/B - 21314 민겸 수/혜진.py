"""
최대 -> 최대한 5가 앞으로 와야함, 뒤에 K가 없으면 M은 하나씩 1이 되도록
1. M 쌓기
2. K 나오면
    M이 있으면: 5 + (0 * M수)
    M 없으면: 5
3. 다 돌고 M수가 있으면 모두 1로

최소 -> 최대한 5가 뒤에 와야함, 뒤에 K가 없으면 M은 한방에 계산
1. M 쌓기
2. K 나오면
    M이 있으면: 1 + (0 * M수 - 1) + 5
    M 없으면: 5
3. 다 돌고 M수가 있으면 한방에 계산
"""

mks = input()

MAX = MIN = ""
mCnt = 0
for mk in mks:
    if mk == "M":
        mCnt += 1
    else:
        if mCnt:
            MAX += "5" + "0" * mCnt
            MIN += "1" + "0" * (mCnt - 1) + "5"
            mCnt = 0
        else:
            MAX += "5"
            MIN += "5"
if mCnt:
    MAX += "1" * mCnt
    MIN += "1" + "0" * (mCnt - 1)

print(MAX)
print(MIN)
