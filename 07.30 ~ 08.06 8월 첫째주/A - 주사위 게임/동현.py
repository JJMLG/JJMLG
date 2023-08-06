def solution(a, b, c, d):
    answer = 0
    if  a==b and a==c and a==d:
        answer = 1111*a
        
    elif a==b and a==c and a!=d:
        answer = (10*a+d)**2
    elif a==c and a==d and a!=b:
        answer = (10*a+b)**2
    elif a==d and a==b and a!=c:
        answer = (10*a+c)**2
    elif b==c and b==d and b!=a:
        answer = (10*b+a)**2
    
    elif a==b and a!=c and a!=d and c==d:
        answer = (a+c) * abs(a-c)
    elif a==c and a!=b and a!=d and b==d:
        answer = (a+b) * abs(a-b)
    elif a==d and a!=b and a!=c and b==c:
        answer = (a+b) * abs(a-b)
        
    elif a==b and c!=d:
        answer = c*d
    elif a==c and b!=d:
        answer = b*d
    elif a==d and b!=c:
        answer = b*c
    elif b==c and a!=d:
        answer = a*d
    elif b==d and a!=c:
        answer = a*c
    elif c==d and a!=b:
        answer = a*b
    elif a!=b and a!=c and a!=d and b!=c and b!=d and c!=d:
        answer = min(a,b,c,d)
    return answer