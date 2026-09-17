class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n=len(nums)
        index=0
        for i in range(n) :
            #consider index=jumping capacity
            #If i>index then it can't jump more. Unable to fulfill total array
            if i> index : return False
            #Update index=max(i,i+nums[i])
            index=max(index, i+nums[i])
            #If index>=n-1 then simply break
            if index>=n-1 : break
        #Return True
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna