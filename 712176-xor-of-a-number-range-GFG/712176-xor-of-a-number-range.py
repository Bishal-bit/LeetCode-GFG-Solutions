class Solution:
    def func(self,n) :
        if n%4==0 : return n
        elif n%4==1 : return 1
        elif n%4==2 : return n+1
        else : return 0
    def findXOR(self, l, r):
        # code here
        return self.func(l-1) ^ self.func(r)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna