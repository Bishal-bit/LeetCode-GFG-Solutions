class Solution:
    def func(self, nums: List[int], goal: int) :
        #Edge case: Due to goal-1 it may go to -1 resulting Overflow.
        if goal<0 : return 0
        n=len(nums)
        left=right=0
        sum=ans=0
        while right < n :
            #Calculate Sum
            sum+=nums[right]
            #If sum>goal shrink the window
            while sum>goal :
                sum-=nums[left]
                left+=1
            #Count is actually counting for all subarrays having sum<=goal
            ans+=right-left+1
            right+=1
        return ans

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        #In a single function counting is very hard when we try to shrink window from left.
        #So (<=goal)-(<=goal-1)=(==goal)
        return self.func(nums,goal)-self.func(nums, goal-1)

            


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna