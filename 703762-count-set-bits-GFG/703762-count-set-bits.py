class Solution:
    def setBits(self, n):
        # code here
        #This algorithm is for removing right most set bit
        #No of set bits=No of bits to be removed=Count
        count=0
        while n :
            n=n & (n-1)
            count+=1
        return count


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna