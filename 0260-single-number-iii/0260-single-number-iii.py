class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor1=0
        for it in nums :
            xor1^=it
        #Rightmost is set on 1 set but in both of a,b
        rightmost=xor1 & -xor1
        a=b=0
        for it in nums :
            #Rightmost bit is set : do exor with a
            if it & rightmost : a^=it
            #Rightmost bit is not set : do exor with b
            else : b^=it
        return [a,b]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna