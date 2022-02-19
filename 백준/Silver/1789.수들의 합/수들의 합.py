import sys

S = int(sys.stdin.readline())

res_ = 0
res = []
for i in range(1,S+1):
    res_ += i
    res.append(i)
    if res_ > S :
        print(res[-2])  
        break