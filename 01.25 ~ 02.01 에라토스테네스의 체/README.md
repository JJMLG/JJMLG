# 이름이 왜 이렇게 길어? 이게 뭔데 도대체?🥴

- 고대 그리스의 수학자 에라토스테네스가 만들어 낸 소수(Prime number)를 찾는 방법.
- 이 방법은 마치 체로 치듯이 수를 걸러낸다고 하여 '에라토스테네스의 체'라고 불러요.

https://namu.wiki/w/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98%20%EC%B2%B4

1. 2부터 N까지 True로 구성된 DP리스트를 만들어요
2. 2부터 출발해요
3. 2를 소수에 추가하고, 2의 배수를 전부 False로 바꿔주고 3으로 이동해요
4. 2의 배수 체크에서 3은 등장하지 않았고 여전히 True에요
5. 3을 소수에 추가하고, 3의 배수를 전부 False로 바꿔주고 4로 이동해요
6. 4는 2의 배수 체크에서 False로 값이 변경되었고, 5로 이동해요
7. 를 N까지 반복해요
8. 한 칸 씩 이동하면서 True인 값이 나오면 소수에 추가해줘요
9. 그리고 그 값의 배수를 전부 False로 바꿔줘요

![https://upload.wikimedia.org/wikipedia/commons/b/b9/Sieve_of_Eratosthenes_animation.gif](https://upload.wikimedia.org/wikipedia/commons/b/b9/Sieve_of_Eratosthenes_animation.gif)

***

# 오, 그러면 이걸 어떻게 활용하는데?🤔

- 가장 작은 소수 2부터 N까지 **주어진 범위안의 모든 소수를 빠르게** 구할 수 있어요
- N이 1,000,000을 넘겨도, 모든 범위를 한 바퀴는 돌기 때문에, **지금 보는 수가 소수인지 아닌지** 알 수 있고 이를 이용하여 문제해결에 활용할 수 있어요
- 소수를 구해서 활용해야 하는 문제에서 **강한 무기**가 되어줄거에요

***

# 알겠는데, 그래서 코드로는 어떻게 짜?😵

```python
n = int(input())                     # 소수를 찾을 범위
a = [False,False] + [True]*(n-1)     # 0 ~ n 까지의 숫자 리스트 (False 두개는 0과 1)
primes = []                          # 소수 집합
for i in range(2,n+1):               # 2 ~ n까지 반복
    if a[i]:                         # 2부터 시작, 지워지지 않고 남아있는 소수이면 
        primes.append(i)             # 소수 리스트에 추가
        for j in range(2*i, n+1, i): # 해당 소수의 배수들을 
            a[j] = False             # 리스트에서 전부 False로 만들기

# print(primes)

'''
n = 20 일 경우
primes = [2, 3, 5, 7, 11, 13, 17, 19]
'''
```

**파이썬튜터에서 동작과정을 눈으로 직접 확인할 수 있어요**

[Python Tutor - Visualize Python, Java, JavaScript, C, C++, Ruby code execution](https://pythontutor.com/visualize.html#mode=display)

***

# 근데 왜 그렇게 소수가 중요한거야?🤨

[소수를 찾는 사람들](https://post.naver.com/viewer/postView.nhn?volumeNo=18688735&memberNo=1328891)

[[Why\] 인간은 왜 素數(소수)를 찾아 헤매나](https://www.chosun.com/site/data/html_dir/2008/10/10/2008101001149.html)

- 요약하자면
  - 소수의 불규칙성을 밝혀내고 싶은 호기심
  - 아무도 찾은 적 없는 소수는 그 자체로 최고의 암호
  - 소수를 활용한 암호는 소수를 구해야만 풀 수 있기 때문
