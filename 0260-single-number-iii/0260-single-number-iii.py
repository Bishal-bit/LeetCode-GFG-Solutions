class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        exor=0
        for it in nums :
            exor^=it
        #Rightmost is set on 1 where both of a,b differ
        rightmost=exor & -exor
        a=b=0
        for it in nums :
            #Rightmost bit is set : do exor with a
            #Rightmost bit is not set : do exor with b
            if it & rightmost : a^=it
            else : b^=it
        return [a,b]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna