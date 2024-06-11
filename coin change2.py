"""taabvulation"""
'''
def coinchange(coins, amount):
    dp = [0]*(amount+1)
    for i in coins:
        for j in range(i, amount+1):
            dp[j]=1+dp[j-i]
    print(dp)
    return dp[amount]
coins=[1,2,5]
amount=7
print(coinchange(coins,amount))
'''

""" recursion"""
def coinchange(coins,amount):
    LARGE_INT = amount + 1
    memo = {}

    def coinchangerecursive(rem):
        if rem==0:
            return 0
        if rem<0:
            return LARGE_INT
        if rem in memo:
            return memo[rem]
        
        min_coins = LARGE_INT
        for coin in coins:
            result = coinchangerecursive(rem - coin)
            if result != LARGE_INT:
                min_coins = min(min_coins,result+1)

        memo[rem] = min_coins
        return memo[rem]
    result = coinchangerecursive(amount)
    return result if result != LARGE_INT else -1
coins = [1,2,5]
amount = 7
print(coinchange(coins,amount))


