import sys

def fibo(n):
    dic[str(n)]=dic.get(str(n-1)) + dic.get(str(n-2)) 

N = int(sys.stdin.readline())

dic = {'0':0, '1':1}

for i in range(2,N+1):
    fibo(i)

print(dic.get(f'{str(N)}'))