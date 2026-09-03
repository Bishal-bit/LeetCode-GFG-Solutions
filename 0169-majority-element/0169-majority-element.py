class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Initialize el as None and count as 0
        el=None
        count=0
        for it in nums :
            #If count==0 reinitialize el as it and set count=1
            if count==0 :
                el=it
                count=1
            #If el==it then increment count
            elif el==it : count+=1
            #If el!=it then decrement count
            elif el!=it : count-=1
        #Set count=0
        count=0
        for it in nums :
            if it==el : count+=1
        n=len(nums)
        #If count exceeds n/2 then return element else -1
        return el if count>n/2 else -1


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna