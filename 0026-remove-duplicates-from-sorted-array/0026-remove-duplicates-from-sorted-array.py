class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        for j in range(n) :
            #If new element is detected then copy it to nums[i+1], increment i
            if nums[i]!=nums[j] :
                nums[i+1]=nums[j]
                i+=1
        #We have to return no of unique elements not index. So return i+1
        return i+1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna