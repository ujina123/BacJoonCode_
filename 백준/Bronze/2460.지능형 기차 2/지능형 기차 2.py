import sys

count, stationCount = [],0

for _ in range(10):
    minus, plus = map(int,sys.stdin.readline().split())
    stationCount -= minus
    stationCount += plus

    count.append(stationCount)

print(max(count))