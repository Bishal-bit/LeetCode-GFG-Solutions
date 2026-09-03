class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Declare a map
        mp={}
        #Treverse through the array
        for i, it in enumerate(nums) :
            #Remain= difference b/w current element it and our target
            remain=target-it
            #If remain is there in map then return it's index, rem's index
            if remain in mp : return [i, mp[remain]]
            #Strore mp[it]=i
            mp[it]=i
        


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna