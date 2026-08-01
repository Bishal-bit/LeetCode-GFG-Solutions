class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        left, right=0, n-1
        while left<=right :
            mid=left+ (right-left)//2
            #If target is in mid index then return mid
            if nums[mid]==target : return mid
            #If left---mid portion is sorted
            elif nums[left]<=nums[mid] :
                #If target in in b/w left and mid then shrink the right side
                if nums[left]<=target<nums[mid] : right=mid-1
                #Else shrink left side
                else : left=mid+1
            ##If mid---right portion is sorted
            else : 
                if nums[mid]<target<=nums[right] : left=mid+1
                else : right=mid-1
        #Return -1
        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna