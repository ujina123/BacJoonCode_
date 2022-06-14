import sys
S = list(sys.stdin.readline())

AtoZ = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

res = []
for i in AtoZ:
    if i in S:
        idx = S.index(i)
        res.append(idx)
    else:
        res.append(-1)
print(*res)