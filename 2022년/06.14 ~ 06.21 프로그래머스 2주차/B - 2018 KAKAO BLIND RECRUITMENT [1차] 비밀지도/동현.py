def solution(n, arr1, arr2):
    answer = []
    # a = 9
    
    def convert(a):
        new = []
        while a > 0:
            m = a % 2
            a = a // 2
            new.append(m)
        
        while True:
            if len(new) < n:
                new.append(0)
            else:
                break
        new = new[::-1]
        return new
    new_arr = []
    for i in range(n):
        a = convert(arr1[i])
        b = convert(arr2[i])
        tmp = ''
        # print(a)
        # print(b)
        for j in range(n):
            if a[j] == 0 and  b[j] == 0:
                tmp += ' '
            else:
                tmp += '#'
        
        new_arr.append(tmp)
    
    
        
    return new_arr