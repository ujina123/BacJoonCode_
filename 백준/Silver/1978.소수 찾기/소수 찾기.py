import sys
N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
res = []

for num in nums:
    if num != 1: 
        res_ = 0
        for h in range(2, num):
            if num % h == 0:
                res_ += 1 
            
        if res_ == 0:
            res.append(num)
print(len(res))