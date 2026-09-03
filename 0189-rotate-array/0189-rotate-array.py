class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        #k might be more than n. So k%=n
        k%=n
        #Reverse the whole list
        nums.reverse()
        #Reverse from 0 to (k-1) th index elements
        nums[:k]=reversed(nums[:k])
        #Reverse from k to n-1 th index elements
        nums[k:]=reversed(nums[k:])
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna