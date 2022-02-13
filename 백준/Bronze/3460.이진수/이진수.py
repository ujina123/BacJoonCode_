import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    res = []
    bi = []
    q, r = divmod(N, 2)
    bi.append(r)

    while q > 1:
        q , r = divmod(q,2)
        bi.append(r)
        
    bi.append(q)

    res = [i for i in range(len(bi)) if bi[i]==1]

    print(*res) 