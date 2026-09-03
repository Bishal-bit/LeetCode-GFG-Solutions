class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        #Declare a map 
        freq={}
        #Traverse through the list pass elements to freq based on frequency
        for it in nums :
            if it in freq : freq[it]+=1
            else : freq[it]=1
        ans=[]
        #Store keys, having value > n/3
        for key, value in freq.items() :
            if value > n/3 : ans.append(key)
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna