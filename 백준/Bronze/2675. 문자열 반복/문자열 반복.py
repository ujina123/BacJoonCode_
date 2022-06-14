T = int(input())
for t in range(T):
    res = []
    R, S = input().split()
    s_list = list(S)
    for s in s_list:
        res.append(s * int(R))
    print(*res, sep='')