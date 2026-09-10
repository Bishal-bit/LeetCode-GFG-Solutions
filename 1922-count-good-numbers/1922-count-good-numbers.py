class Solution:
    def countGoodNumbers(self, n: int) -> int:
        #Considering 4 digits having,
        #5 choices for even positions 0,2,4,6,8
        #4 choices for odd positions 2,3,5,7
        mod=10**9+7
        even=(n+1)//2       #5 Choices
        odd=n//2            #4 Choices
        return (pow(5, even, mod)*pow(4, odd, mod))%mod

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna