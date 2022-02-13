import sys

res = []
for _ in range(int(input())):
    N = int(sys.stdin.readline())
    if N != 0 :
        res.append(N)
    else:
        res.pop()
        
print(sum(res))