class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*n
        pos,neg=0,1
        #Traverse through the array push (+)ves to pos, ()ves to neg index 
        #Increment indices by 2
        for it in nums :
            if it>0 : 
                ans[pos]=it
                pos+=2
            else : 
                ans[neg]=it
                neg+=2

        return ans
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna