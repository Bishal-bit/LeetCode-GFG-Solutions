class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Binary Search
        n=len(nums)
        low, high=0, n-1
        while(low<=high) :
            mid=low+ (high-low)//2
            if nums[mid]==target : return mid
            elif nums[mid]<target : low=mid+1
            else : high=mid-1
        #Return -1
        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna