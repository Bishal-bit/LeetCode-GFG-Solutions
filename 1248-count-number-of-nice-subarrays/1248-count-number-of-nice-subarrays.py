class Solution:
    def func(self, nums: List[int], k: int) :
        if k<0 : return 0
        n=len(nums)
        left=right=0
        count=0
        while right<n :
            #If odd then decrement k
            if nums[right]%2==1 : k-=1
            #While k<0 : 
            #           if nums[left] is odd then increment k
            #           increment left
            while k<0 :
                if nums[left]%2==1 : k+=1
                left+=1
            #Update count, increment count
            count+=right-left+1
            right+=1
        #Return count
        return count
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        #In a single function counting is very hard when we try to shrink window from left.
        #So (Subarrays<=k odd nos)-(<=k-1 odd nos)=(Subarrays==k odd nos)
        return self.func(nums, k)-self.func(nums, k-1)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna