import sys

def push(num):
    res.append(int(num))
    return res

def pop():
    if len(res) == 0:
        print(-1)
    else: 
        print(res[-1])
        res.pop()
        
def empty():
    if len(res) == 0:
        print(1)
    else:
        print(0)

def top():
    if len(res) == 0:
        print(-1)
    else: 
        print(res[-1])

N = int(sys.stdin.readline())
res = []

for _ in range(N):
    func = sys.stdin.readline().strip()
    if func.find('push') == 0:
        push(func[4:])
    elif func == 'pop': pop()
    elif func == 'top': top()
    elif func == 'size': print(len(res))
    elif func == 'empty': empty()