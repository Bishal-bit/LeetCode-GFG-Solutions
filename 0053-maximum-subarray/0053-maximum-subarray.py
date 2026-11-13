class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        #Kadane's Algorithm
        #Initialize sum as 0, maxi as float('-inf')
        sum=0
        maxi=float('-inf')
        for it in nums :
            sum+=it                 #Adding elements to sum
            maxi=max(maxi, sum)     #Update maxi, based on max value
            if sum<0 : sum=0        #If sum<0 then reinitialize sum as 0
        #Return maxi    
        return maxi
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna