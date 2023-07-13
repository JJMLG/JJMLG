def solution(order):
    st = []
    o = 0
    for i in range(1, len(order) + 1):
        st.append(i)
        while st and st[-1] == order[o]:
            o += 1
            st.pop()
    return o
