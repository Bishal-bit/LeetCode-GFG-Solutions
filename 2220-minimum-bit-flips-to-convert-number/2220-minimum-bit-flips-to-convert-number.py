class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        #Change is the change of bits between start and goal
        change=start ^ goal
        count=0
        #Count set bits of change
        while change :
            if change & 1 : count+=1
            change>>=1
        #Return count
        return count


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna