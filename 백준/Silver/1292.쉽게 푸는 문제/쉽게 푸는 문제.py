import sys
start, last = map(int,sys.stdin.readline().split())

res = 0
list = []
for num in range(1,last+1):
    for _ in range(num):
        list.append(num)
        if len(list) == last+1:
            break

for i in range(start-1,last):
    res += list[i]
    
print(res)