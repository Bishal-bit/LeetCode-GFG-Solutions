class Solution:
    def setBit(self, n):
        # code here
        #if we go from n to (n+1) the right most unset bit of n is to be changed
        # 011-->100-->101-->110
        return n | (n+1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna