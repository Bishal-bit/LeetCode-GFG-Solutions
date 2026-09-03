class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #Initialize one as 0 and maxi as float('-inf')
        one, maxi=0, float('-inf')
        for it in nums :
            #If it is 1 then increment one 
            if it==1 : one+=1
            #If it is 0 then make one as 0
            elif it==0 : one=0
            #Update maxi
            maxi=max(maxi, one)
        #Return maxi
        return maxi

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna