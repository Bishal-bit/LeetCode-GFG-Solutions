class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<1 : return False
        if n & (n-1) ==0 : return True
        return False 
       

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna