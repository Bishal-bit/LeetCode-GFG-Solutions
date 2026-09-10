class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        # 2^n So, 0----2^n-1
        for i in range(1<<n) :
            v=[]
            #List element indices
            for it in range(n) :
                if i & 1<<it : v.append(nums[it])
            ans.append(v.copy())
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna