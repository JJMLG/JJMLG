def solution(numbers):
    answer = []
    for number in numbers:
        if number % 2 == 0:
            answer.append(number+1)
        else:
            n = bin(number)[2:][::-1] + '0' 
            zero = n.find('0') 
            n = (n[:zero-1]+'01'+n[zero+1:])[::-1] 
            answer.append(int(n, 2))
            
    return answer