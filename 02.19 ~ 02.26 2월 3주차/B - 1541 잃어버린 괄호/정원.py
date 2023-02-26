def new_sum(exp):
    plus_split = exp.split('+')
    answer = 0

    for i in range(len(plus_split)):
        answer += int(plus_split[i])

    return answer

exps = input()
minus_split = exps.split('-')
result = new_sum(minus_split[0])

for a in minus_split[1:]:
    result -= new_sum(a)

print(result)