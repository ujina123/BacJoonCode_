import sys

N = 3
T = int(sys.stdin.readline())

res = []

for _ in range(T):
    A = list(map(int,sys.stdin.readline().split()))
    res.append(sorted(A,reverse=True)[N-1])

[print(i) for i in res]