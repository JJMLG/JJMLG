def solution(n):
    ans = 1
    while n > 1:
        if n % 2:
            n -= 1
            ans += 1
        else:
            n //= 2
    return ans
