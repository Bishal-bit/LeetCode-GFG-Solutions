class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        left=mid=0
        right=n-1
        while mid<=right :
            #If nums[mid]==0 then swap nums[left], nums[mid]
            #Increment left, mid
            if nums[mid]==0 :
                nums[left], nums[mid]=nums[mid], nums[left]
                left+=1
                mid+=1
            #If nums[mid]==1 increment mid
            elif nums[mid]==1 : mid+=1
            #Else i.e. nums[mid]==2 then swap nums[mid],nums[right]
            #Decrement right
            else :
                nums[mid], nums[right]=nums[right], nums[mid]
                right-=1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna