N, M = map(int, input().split()) # DNA의 개수 N과 길이 M

DNAs = [input() for _ in range(N)] # DNA들을 담은 리스트

dictt = { # DNA는 ACGT 네가지로 구성되며, 각각의 인덱스를 지정
    # 딕셔너리를 숫자<->문자 양방향으로 만들지 않고
    # 한 쪽은 키값, 다른 한 쪽은 밸류값 썼으면 됐는데 귀찮았습니다 ㅈㅅ...
    'A': 0,
    'C': 1,
    'G': 2,
    'T': 3,
    0: 'A',
    1: 'C',
    2: 'G',
    3: 'T',
}

HD = 0 # Hamming Distance, 구하고자 하는 값

for i in range(M): # DNA의 길이만큼

    table = [0] * 4 # ACGT

    # 모든 DNA의 i번째 글자에 대하여, 가장 많이 등장한 DNA값이
    # 가장 최소의 Hamming Distance값을 가지게 됨
    for d in DNAs: # 각각의 DNA의 글자 마다
        table[dictt[d[i]]] += 1
        # d[i] = 각 DNA의 i번째 글자
        # dictt[d[i]] = d[i]를 ACGT에 맞게 인덱스로 변환한 값
        # table[dictt[d[i]]] = table에서 d[i]를 변환한 인덱스값에 해당하는 칸
        # ex) d = TATGATAC, i = 0 일 때, d[i] = 'T'
        # dictt[d[i]] = dictt['T'] = 3
        # table[dictt[d[i]]] = table[3]
        # table[3] += 1 이 실행됨
        
    # 최소 Hamming Distance값을 구하자
    for j in range(4): # 테이블 순회
        if j != table.index(max(table)): # Hamming Distance가 아닌 DNA일때
            HD += table[j] # 그 DNA가 등장한 횟수를 Hamming Distance에 더하기

    print(dictt[table.index(max(table))], end='') 
    # 매 i에 대하여 Hamming Distance가 되는 DNA글자를 구하였고 이를 출력

print() # 줄바꿈

print(HD) # 최소 Hamming Distance값
