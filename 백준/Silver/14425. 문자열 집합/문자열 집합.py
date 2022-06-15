import sys

N, M = map(int,input().split())
cnt = 0
NList = set()

for _ in range(N):
    N_input = sys.stdin.readline()
    NList.add(N_input)

for _ in range(M):
    VOCA = sys.stdin.readline()
    if VOCA in NList:
        cnt += 1

print(cnt)