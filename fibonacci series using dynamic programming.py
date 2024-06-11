count=0
def fib(n,memo):  #top to bottom approach
    global count
    if n<=1:
       count=count+1
       return n
    
    if memo[n]!=-1:
        count=count+1
        return memo[n]
    
    memo[n] = fib(n-1,memo)+fib(n-2,memo)
    count=count+1
    return memo[n]

n=10
memo=[-1]*(n+1)
#memo[0]=0
#memo[1]=1
print(fib(n,memo))
print(memo)
print(count)