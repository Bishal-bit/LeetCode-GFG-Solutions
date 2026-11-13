class Solution:
    def climbStairs(self, n: int) -> int:
        #Do dry run
        if n<=2 : return n
        dp=[0] * (n+1)          #(n+1) because ans is to be stored at dp[n]
        #You can reach final position via 1 step or 2 step
        #Step--No of distinct ways
        #0-0    1-1     2-2 
        #3-3    4-5     5-8     6-13
        dp[1], dp[2]=1, 2
        for i in range(3, n+1) :
            dp[i]=dp[i-1]+ dp[i-2]
        #Return dp[n]
        return dp[n]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna