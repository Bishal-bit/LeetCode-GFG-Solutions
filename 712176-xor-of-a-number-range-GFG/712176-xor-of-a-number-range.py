class Solution:
    def func(self, x: int) :
        if x%4==0 : return x
        elif x%4==1 : return 1
        elif x%4==2 : return x+1
        else : return 0
        
    def findXOR(self, l, r):
        # code here
        #0----l----r
        #We want exor of l----r
        # exor of 0---l-1 exor of 0---r => exor of l---r
        return self.func(l-1) ^ self.func(r) 


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna