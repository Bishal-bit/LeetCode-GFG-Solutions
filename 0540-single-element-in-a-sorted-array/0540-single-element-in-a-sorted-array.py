class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1 : return nums[0]
        if nums[0]!=nums[1] : return nums[0]
        if nums[n-1]!=nums[n-2] : return nums[n-1]
        left, right=1, n-2
        while left<= right :
            mid=left+ (right-left)//2
            if nums[mid-1]!=nums[mid]!=nums[mid+1] : return nums[mid]
            #Left Half of Array.
            elif (mid%2==0 and nums[mid]==nums[mid+1]) or (mid%2==1 and nums[mid]==nums[mid-1]) : left=mid+1
            #Right Half of Array.
            else : right=mid-1
        return -1
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna