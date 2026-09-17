class Solution:
    def jump(self, nums: list[int]) -> int:
        n=len(nums)
        #If n==1 no jump required
        if n==1 : return 0
        count=current=furthest=0
        #By the time we reach n-2, our current>=n-1.
        #Our intension is to reach up to n-1, not to process n-1. So for(i=0 to n-2)
        for i in range(n-1) :
            #consider index=jumping capacity
            furthest=max(furthest, i+nums[i])
            #As we see current is to be updated with furthest.
            #So when i==current i.e. i reaches to it's furthest range, increment count,update current
            if i==current :
                count+=1
                current=furthest
        #Return count
        return count
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna