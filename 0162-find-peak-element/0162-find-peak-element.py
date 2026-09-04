class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        #If Length=1 then return 0
        if n==1 : return 0
        #0th index element is greater than 1st index then return 0
        if nums[0]>nums[1] : return 0
        #(n-1)th index element is greater than (n-2)th index then return n-1
        if nums[n-1]>nums[n-2] : return n-1
        left, right=1, n-2
        while left<=right :
            mid=left+ (right-left)//2
            #mid is greater than mid-1 and mid+1 then return mid
            if nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1] : return mid
            #mid-1 is smaller then update left
            elif nums[mid-1]<nums[mid] : left=mid+1
            #mid-1 is greater then update right
            else : right=mid-1
        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna