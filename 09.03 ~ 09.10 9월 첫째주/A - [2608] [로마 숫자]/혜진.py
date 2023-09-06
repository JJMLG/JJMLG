import sys
sys.stdin = open('input.txt')

def makeNum(word):
    num = 0
    dic = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
    """
    IV: V - I = 5 - 1 = 4
    IX: X - I = 10 - 1 = 9
    XL: L - X = 50 - 10 = 40
    XC: C - X = 100 - 10 = 90
    CD: D - C = 500 - 100 = 400
    CM: M - C = 1000 - 100 = 900
    """
    for i in range(len(word)):
        if i + 1 < len(word) and dic[word[i]] < dic[word[i + 1]]:
            num -= dic[word[i]]
        else:
            num += dic[word[i]]
    return num

num = makeNum(input()) + makeNum(input())
print(num)

ans = ''
while num:
    if num // 1000 > 0:
        tmp = num // 1000
        num %= 1000
        ans += 'M' * tmp

    elif num // 100 > 0:    # 900, 500, 400, n00
        tmp = num // 100
        num %= 100
        if tmp == 9:
            ans += 'CM'
        elif tmp == 5:
            ans += 'D'
        elif tmp == 4:
            ans += 'CD'
        elif tmp > 5:
            ans += 'D'
            ans += 'C' * (tmp - 5)
        elif tmp < 5:
            ans += 'C' * tmp

    elif num // 10 > 0:     # 90, 50, 40, n0
        tmp = num // 10
        num %= 10
        if tmp == 9:
            ans += 'XC'
        elif tmp == 5:
            ans += 'L'
        elif tmp == 4:
            ans += 'XL'
        elif tmp > 5:
            ans += 'L'
            ans += 'X' * (tmp - 5)
        elif tmp < 5:
            ans += 'X' * tmp

    else:                   # 9, 5, 4, n
        if num == 9:
            ans += 'IX'
        elif num == 5:
            ans += 'V'
        elif num == 4:
            ans += 'IV'
        elif num > 5:
            ans += 'V'
            ans += 'I' * (num - 5)
        elif num < 5:
            ans += 'I' * num
        break

print(ans)
