class Solution:
    def func(self, nums: List[int], k: int ) :
        #Sliding Window
        n=len(nums)
        #Declare a map mp to record frequency of integers
        mp={}
        left, ans=0, 0
        for right in range(n) :
            #If it is a new integer i.e. not present in map mp then decrement k
            if nums[right] not in mp : k-=1
            mp[nums[right]]=mp.get(nums[right],0)+1
            #While k<0 : shrink window from left side
            while k<0 :
                mp[nums[left]]-=1
                if mp[nums[left]]==0 : 
                    mp.pop(nums[left])
                    k+=1
                left+=1
            #Update ans
            ans+=right-left+1
        return ans

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        #In a single function counting is very hard when we try to shrink window from left.
        #So (Subarrays <=k different nos)-(<=k-1 different nos)=(Subarrays==k different nos)
        return self.func(nums, k) - self.func(nums, k-1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna