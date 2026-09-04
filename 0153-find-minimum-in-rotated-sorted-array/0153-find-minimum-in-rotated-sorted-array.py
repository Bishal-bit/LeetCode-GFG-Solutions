class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        mini=float('inf')
        left, right=0, n-1
        while left<= right :
            mid=left+ (right-left)//2
            #If whole list is sorted left---mid---right
            #Update mini and break
            if nums[left]<= nums[right] : 
                mini=min(mini, nums[left])
                break

            #if left---mid portion is sorted
            #Update mini then check for right portion by updating left
            elif nums[left]<= nums[mid] :
                mini=min(mini, nums[left])
                left=mid+1

            #if mid---right portion is sorted
            #Update mini then check for left portion by updating right
            else:
                mini=min(mini, nums[mid])
                right=mid-1
        #Return mini
        return mini
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna