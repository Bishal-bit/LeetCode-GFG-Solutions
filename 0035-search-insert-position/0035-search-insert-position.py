class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        low, high=0, n-1
        #Initialize ans as n in case no element is greater than target
        ans=n
        while low<=high :
            #Calculate mid
            mid=low + (high-low)//2
            #If nums[mid]>=target then update ans as mid and check the left portion by high=mid-1
            if nums[mid]>=target :
                ans=mid
                high=mid-1
            #Else update low as mid+1
            else :
                low=mid+1
        return ans


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna