class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ """
        Find pivot (index)
        If pivot exists :   From suffix take the element(i) greater than pivot
                            Swap them
        Reverse the suffix
        Ex: 1 2 7 4 3 1     
            pivot=1, nums[pivot]=2
            nums[i]=3
            swap
            1 3 7 4 2 1
            reverse the suffix
            1 3 1 2 4 7

        """
        n=len(nums)
        pivot=n-2
        while pivot >=0 and nums[pivot]>=nums[pivot+1] : pivot-=1
        #If pivot exist then find nums[i] to do swap operation
        if pivot>=0 :
            i=n-1
            while nums[i]<=nums[pivot] : i-=1
            nums[pivot], nums[i]=nums[i] , nums[pivot]
        left, right=pivot+1, n-1
        while left<=right :
            nums[left] ,nums[right]=nums[right] ,nums[left]
            left+=1
            right-=1
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna