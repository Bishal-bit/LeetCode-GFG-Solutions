class Solution:
    def myPow(self, x: float, n: int) -> float:
        n1=n
        if n<0 : n1=-1 *n
        ans=1
        while n1>0 :
            if n1%2==0 :    #n1 as even
                x*=x
                n1//=2
            else :          #n1 as odd
                ans*=x
                n1-=1
        
        if n<0 : return 1/ans
        return ans

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna