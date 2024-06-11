s=[1,2,3,4,5]
s1=[]

def isempty(s):
    if len(s)==0:
        return True
    else:
        return False
def display(s):
    while isempty(s)!=True:
        print(s.pop())
def push(s,data):
    s.append(data)

while isempty(s)!=True:
   push(s1,s.pop())

   
    
display(s1)


        
