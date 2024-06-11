# letter combination of a phone number
class Solution(object):
    
    def lettercombination(self,digits):
        res = []
        digits_to_letters = {
        '2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxy',}
        def backtrack(i,comb):
            if len(comb)==len(digits):
                res.append(comb)
                return
            for c in digits_to_letters[digits[i]]:
                backtrack(i+1,comb+c)
        if digits:
            backtrack(0,"")
        return res


c=Solution()
print(c.lettercombination("23"))
