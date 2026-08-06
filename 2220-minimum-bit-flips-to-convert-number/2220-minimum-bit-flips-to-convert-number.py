class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        change=start ^ goal
        count=0
        while change :
            if change & 1 ==1 : count+=1
            change>>=1
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna