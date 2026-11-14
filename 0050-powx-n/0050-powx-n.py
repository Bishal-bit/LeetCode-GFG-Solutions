class Solution:
    def myPow(self, x: float, n: int) -> float:
        sign=1
        ans=1
        if n<0 :
            sign=-1
            n=(-1)*n
        while n :
            if n%2==0 : 
                x*=x
                n//=2
            else : 
                ans*=x
                n-=1
        if sign==-1 : return 1/ans
        return ans
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna