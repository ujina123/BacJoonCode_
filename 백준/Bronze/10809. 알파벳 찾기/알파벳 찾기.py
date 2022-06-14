S = list(input())
b = [-1 for _ in range(26)]
for i in S:
    n = ord(i)-97
    if b[n] != -1:
        continue
    b[n] = S.index(i)
print(*b)