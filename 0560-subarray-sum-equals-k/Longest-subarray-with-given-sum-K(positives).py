class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #2 Pointer approach
        left=right=0
        maxlen=0
        n=len(nums)
        #Initialize 0th element of nums to sum
        sum=nums[0]
        while(right<n) :
            #If sum exceeds k and left<=right then shrink the window from left side
            while(left<=right and sum>k) :
                sum-=nums[left]
                left+=1
            #If sum==k then update maxlen by using left,right pointers
            if(sum==k) : maxlen=max(maxlen,right-left+1)
            #Increment right
            right+=1
            #If right does not exceed list then add it's value to sum
            if(right<n) : sum+=nums[right]
        #Return maxlen
        return maxlen

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
