def find(n):
    s, e = 0, N1 - 1
    while s <= e:
        m = (s + e) // 2
        if nums1[m] == n:
            return 1
        if n <= nums1[m]:
            e = m - 1
        else:
            s = m + 1
    return 0

for _ in range(int(input())):
    N1 = int(input())
    nums1 = sorted(map(int, input().split()))
    N2 = int(input())
    nums2 = list(map(int, input().split()))
    for n in nums2:
        print(find(n))
