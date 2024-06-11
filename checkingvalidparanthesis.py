ch="[({()})]"

def push(s,data):
    s.append(data)

def top(ch):
    return ch[-1]

def isempty(ch):
    if len(ch)==0:
        return True
    else:
        return False
def check(ch):
    s=[]
    for i in range(len(ch)):
        if ch[i] in "{([":
            push(s,ch[i])
        elif (ch[i]==")" and top(s)=="(") or (ch[i]=="]" and top(s)=="[") or (ch[i]=="}" and top(s)=="{"):
            s.pop()
        else:
            break
    if isempty(s)==True:
        print("valid")
    else:
        print("invalid")

check(ch)

