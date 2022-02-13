import sys
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

res = []
for num in range(M,N+1):
    if num != 1 :
        sosu = 0
        for n in range(2,num):
            if num % n == 0:
                sosu += 1
            if sosu != 0:
                break
        if sosu == 0:
            res.append(num)

print(-1) if len(res) == 0 else print(f'{sum(res)}\n{min(res)}')