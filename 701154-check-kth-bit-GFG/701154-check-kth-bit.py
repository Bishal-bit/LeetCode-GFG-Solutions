class Solution:
    def checkKthBit(self, n, k):
        # code here
        #kth digit is 1, rest of the right side digits are 0
        val=1<<k
        return (n & val)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna