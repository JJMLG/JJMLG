giho = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

twoLetter =  {
    "IV" : 4, "IX" : 9, "XL" : 40, "XC" : 90, "CD" : 400, "CM" : 900
}
a = input()
b = input()

def getNumber(a):
    calculated = [0]*len(a)
    value = 0
    for i in range(len(a)):
        if calculated[i] == 0:
            if i == len(a)-1:
                value += giho[a[i]]
                break
            if giho[a[i]] >= giho[a[i+1]]:
                value += giho[a[i]]
            else:
                value += twoLetter[a[i]+a[i+1]] 
                calculated[i+1] = 1
    return value

num = getNumber(a) + getNumber(b)

print(num)
rome =""

# mm 조건 의미없음;
while num >0 :
    if num >= 1000 and (len(rome) > 1 and rome[len(rome)-2:len(rome)-1]) != "MM":
        rome += "M"
        num -= 1000
    elif num >= 900:
        rome += "CM"
        num -= 900
    elif num >= 500:
        rome += "D"
        num -= 500
    elif num >= 400:
        rome += "CD"
        num -= 400
    elif num >= 100 and (len(rome) > 1 and rome[len(rome)-2:len(rome)-1]) != "CC":
        rome += "C"
        num -= 100
    elif num >= 90:
        rome += "XC"
        num -= 90
    elif num >= 50:
        rome += "L"
        num -= 50
    elif num >= 40:
        rome += "XL"
        num -= 40
    elif num >= 10 and (len(rome) > 1 and rome[len(rome)-2:len(rome)-1]) != "XX":
        rome += "X"
        num -= 10
    elif num >= 9:
        rome += "IX"
        num -= 9
    elif num >= 5:
        rome += "V"
        num -= 5
    elif num >= 4:
        rome += "IV"
        num -= 4
    elif num >= 1 and (len(rome) > 1 and rome[len(rome)-2:len(rome)-1]) != "II":
        rome += "I"
        num -= 1

print(rome)


# getValue(b)
# temp = getValue(a) + getValue(b)

# print(temp)



    
# 큰 숫자가 왼쪽, 작은 숫자가 오른쪽
# V,L,D는 한 번 사용, I,X,C,M은 연속 세번 까지
# 작은 숫자가 큰 숫자의 왼쪽에 오는경우, IV = 4, IX = 9, XL = 40, XC = 90, CD = 400, CM = 900  (한번 사용)
# IV 와 IX 는 같이 쓸 수 없으며 XL 과 XC, CD 와 CM 또한 같이 쓸 수 없다
# 모든 수는 가능한 가장 적은 개수의 로마 숫자들로 표현

