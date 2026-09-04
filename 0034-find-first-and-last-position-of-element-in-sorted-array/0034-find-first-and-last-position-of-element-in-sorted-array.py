class Solution:
    def first1(self, nums : List[int], target: int) :
        n=len(nums)
        left, right=0, n-1
        ans=-1
        while left<= right :
            mid=left+ (right-left)//2
            if nums[mid]==target :
                #Update ans and check for left side portion by updating right
                ans=mid
                right=mid-1
            elif nums[mid]<target : left=mid+1
            else : right=mid-1
        return ans
    
    def last1(self, nums : List[int], target: int) :
        n=len(nums)
        left, right=0, n-1
        ans=-1
        while left<= right :
            mid=left+ (right-left)//2
            if nums[mid]==target :
                #Update ans and check for right side portion by updating left
                ans=mid
                left=mid+1
            elif nums[mid]<target : left=mid+1
            else : right=mid-1
        return ans
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a=self.first1(nums, target)
        #If first index is not found then no need to find the second index
        if a==-1 : return [-1, -1]
        b=self.last1(nums, target)
        return [a, b]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna