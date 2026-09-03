class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        exor1=0
        for it in nums :
            exor1^=it
        return exor1



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna