import sys
K = int(sys.stdin.readline())

res = []
for _ in range(K):
    gwalho_res = []

    gwalho = sys.stdin.readline()
    
    for g in gwalho:
        if g == '(':
            gwalho_res.append(g)
        elif g == ')':
            if len(gwalho_res) == 0:
                gwalho_res.append(g)
                break
            elif len(gwalho_res) != 0:
                gwalho_res.pop()
                
    if len(gwalho_res) == 0:
        res.append('YES')
    else:
        res.append('NO')

for i in res:
    print(i)