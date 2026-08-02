class Solution:
    def largestOddNumber(self, num: str) -> str:
        #If already a odd no then return it
        if int(num[-1])%2==1 : return num
        n=len(num)
        #Finding index of last odd no
        for i in range(n-1,-1,-1) :
            if int(num[i])%2==1 : break
        #0--0. Only one digit that is 0th digit. If it is even then return empty string
        if i==0 and int(num[i])%2==0 : return ""
        #Return substring 0--i
        return num[:i+1]
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna