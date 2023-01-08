num = [int(input()) for _ in range(2)]
if num[0]>0 and num[1]>0:
    print(1)
elif num[0]<0 and num[1]>0:
    print(2)
elif num[0] > 0 and num[1] < 0:
    print(4)
else:
    print(3)