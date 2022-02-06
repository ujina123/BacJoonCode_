import sys

N = int(sys.stdin.readline().strip())
numList = list(map(int,sys.stdin.readline().split()))
print(min(numList), max(numList))