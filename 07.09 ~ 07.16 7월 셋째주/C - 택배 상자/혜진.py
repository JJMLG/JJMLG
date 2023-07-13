def solution(order):
    st = []
    o = 0
    for i in range(1, len(order) + 1):      # i는 1부터 order의 길이까지
        st.append(i)                        # 일단 넣기
        while st and st[-1] == order[o]:    # 스택 마지막과 주문이 같으면
            st.pop()      # pop하고
            o += 1        # 다음 주문
    return o              # 주문 어디까지
