class Solution:
    def leaders(self, arr):
        # code here
        n=len(arr)
        ans=[]
        maxi=float('-inf')
        #Treverse in reverse order
        for i in range(n-1,-1,-1) :
            #If element>=maxi then update maxi and append to ans
            if arr[i]>=maxi :
                maxi=arr[i]
                ans.append(maxi)
        #Reverse ans
        ans.reverse()        
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna