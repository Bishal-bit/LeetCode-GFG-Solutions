class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while n :
            #Check last digit is set or not
            if n & 1 : count+=1
            #Shift one digit to right. It actually eleminates last digit
            n>>=1
        return count
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna