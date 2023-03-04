def make4(ip):
    more = 4 - len(ip)
    if more:
        return '0' * more + ip
    return ip

ip6 = input().split(':')
if ip6[0] == '':
    ip6.pop(0)
elif ip6[-1] == '':
    ip6.pop(-1)

ans = []
for ip in ip6:
    if ip == '':
        for _ in range(8 - len(ip6) + 1):
            ans.append('0000')
    else:
        ans.append(make4(ip))

print(':'.join(ans))
