class Solution:
    def func(self, index :int, nums: List[int], n: int, v: List[int], ans :List[List[int]]) :
        #There is no constraints for the v that is why no if condition. Direct statement
        ans.append(v.copy())
        for i in range(index, n) :
            #If same element repeated in nums then skip
            if i>index and nums[i]==nums[i-1] : continue
            #After appending element in v, go for next index
            v.append(nums[i])
            self.func(i+1, nums, n, v, ans)
            #Backtracking
            v.pop()


    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        #Sort elements of nums
        nums.sort()
        ans=[]
        self.func(0, nums, n, [], ans)
        return ans
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna