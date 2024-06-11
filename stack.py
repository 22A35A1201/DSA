s=[]
#push
s.append(1)
s.append(2)

def push(data):
    s.append(data)

push(3)
push(4)
push(5)
push(6)

def top():
    return s[-1]
a=top()
print(a)
print(s)
