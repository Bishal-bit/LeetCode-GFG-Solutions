class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Initialize element as None and count as 0
        element=None
        count=0
        for it in nums :
            #If count==0 reinitialize element as it and set count=1
            if count==0 :
                element=it
                count=1
            #If it==element then increment count
            elif it==element : count+=1
            #If it!=element then decrement count
            elif it!=element : count-=1
        #Set count=0
        count=0
        for it in nums :
            if it==element : count+=1
        n=len(nums)
        #If count exceeds n/2 then return element
        if count>n/2 : return element

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna