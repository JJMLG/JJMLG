
def next_permutation():
        #꼭대기 값 찾기
        i=N-1
        while(i>0 and arr[i-1]>=arr[i]):
            i-=1

        if i==0: #내림차순 정렬 완료
            return False

        #꼭대기-1보다 큰 값 찾기
        #꼭대기+1~오른쪽 끝 값 중 큰 값이 없으면 꼭대기 값이랑 바꾼다
        j=N-1
        while(arr[i-1]>=arr[j]):
            j-=1
        arr[i-1], arr[j] = arr[j], arr[i-1]

        #꼭대기 ~ 끝까지 reverseOrder
        k=N-1
        while(i<k):
            arr[i], arr[k] = arr[k], arr[i]
            i+=1
            k-=1

        return True


n = int(input())
for _ in range(n):
    s = input()
    N= len(s)
    arr=list(s)

 

    if not next_permutation():
        print(s)

    else:
        tmp = ""
        for i in range(N):
            tmp += arr[i]
        print(tmp)