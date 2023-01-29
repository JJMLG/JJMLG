import sys
sys.stdin = open("input.txt")

T= int(input())
numberToString = {
    0:"ZERO", 2:"TWO", 4:"FOUR", 6:"SIX", 8:"EIGHT",
    3:"THREE",5:"FIVE", 7:"SEVEN", 9:"NINE", 1:"ONE"
}
def checkInside(num):
    for letter in numberToString[num]:
        if not letter in stringCount:
            return 0
        if stringCount[letter] < numberToString[num].count(letter):
            return 0

    for letter in numberToString[num]:
        stringCount[letter]-=1
    return 1

for tc in range(1, T+1):
    pb = input()
    stringCount = dict()
    for letter in pb:
        if letter in stringCount:
            stringCount[letter]+=1
        else:
            stringCount[letter]=1
    idx = 0
    result = []
    keys= list(numberToString.keys())
    while idx < 10:
        ret = checkInside(keys[idx])
        if(ret):
            result.append(str(keys[idx]))
        else:
            idx+=1
    result = "".join(sorted(result))
    print("Case #{}: {}".format(tc,result))
