class Solution:
    def check(self, nums: List[int]) -> bool:
        n=len(nums)
        #Initialize count as 0
        count=0
        for i in range(n) :
            #If mismatch happens then increment count
            if nums[i]>nums[(i+1)%n] : count+=1
        #The upper limit of count is 1 to be True else False
        return True if count<=1 else False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna