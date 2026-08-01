class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n=len(nums)
        left, right=0, n-1
        while left<=right :
            mid=left+ (right-left)//2
            #If target is in mid index then return True
            if nums[mid]==target : return True
            
            #Can not retermine which part is sorted due to duplicates
            if nums[left]==nums[mid]==nums[right] :
                left+=1
                right-=1
            
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
        
        #Return False
        return False
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna