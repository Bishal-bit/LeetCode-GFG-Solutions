class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        sum=0       #Initialize sum as 0
        #Count sum for 0th to (k-1)th element
        for i in range(k) : 
            sum+=cardPoints[i]
        #Initialize ans as sum
        ans=sum
        for i in range(k) :
            #Remove one element from (right most)left
            sum-=cardPoints[k-1-i]
            #Adding one element from (right most)right
            sum+=cardPoints[n-1-i]
            #Update ans
            ans=max(ans, sum)
            """
                 left:2 right:6
            then left:1 right:5
            then left:0 right:4
            """
        return ans


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna