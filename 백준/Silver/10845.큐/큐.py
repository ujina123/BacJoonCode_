import sys

def push(num):
    Que_res.append(num)
    
def pop():
    if len(Que_res) == 0:
        print(-1)
    else:
        print(Que_res[0])
        del Que_res[0]

def empty():
    if len(Que_res) == 0: 
        print(1)
    else : 
        print(0)

def front():
    if len(Que_res) == 0: 
        print(-1)
    else: 
        print(Que_res[0])

def back():
    if len(Que_res) == 0:
        print(-1)
    else: 
        print(Que_res[-1])
    
Que_res = []
for _ in range(int(sys.stdin.readline())):
    func = sys.stdin.readline().strip() #split
    if func.find('push') == 0:
        push(func[5:])  
    elif func == 'pop':
        pop() 
    elif func == 'size':    
        print(len(Que_res))
    elif func == 'empty':
        empty()
    elif func == 'front':
        front()
    elif func == 'back':
        back()