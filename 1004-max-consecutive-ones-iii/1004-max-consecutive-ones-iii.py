class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #Sliding Window
        n=len(nums)
        left, right=0, 0
        maxi=0
        while right<n :
            #If nums[right]==1 then increment right
            if nums[right]==1 : right+=1
            #If nums[right]==0 and k then decrement k, increment right
            elif nums[right]==0 and k :  
                k-=1
                right+=1
            #We have to shrink the window by incrementing left
            else :
                #if nums[left]==0 then increment k
                if nums[left]==0 : k+=1
                left+=1
            #Update maxi
            maxi=max(maxi, right-left)
        #Return maxi
        return maxi
                

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna