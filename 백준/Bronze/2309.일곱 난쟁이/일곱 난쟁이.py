import sys

N = 9

ki_list = [int(sys.stdin.readline()) for _ in range(N)]

ki_total = sum(ki_list) - 100 


if ki_total > 0:
    for i in range(len(ki_list)):
        for j in range(len(ki_list)):
            if (ki_list[i] + ki_list[j]) == ki_total and i!=j:
                no_nanjaeng1 = ki_list[i]
                no_nanjaeng2 = ki_list[j]

ki_list.remove(no_nanjaeng1)
ki_list.remove(no_nanjaeng2)

for i in sorted(ki_list):
    print(i)