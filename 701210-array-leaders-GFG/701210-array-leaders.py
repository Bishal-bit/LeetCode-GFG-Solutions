class Solution:
    def leaders(self, arr):
        # code here
        n=len(arr)
        ans=[]
        #Treverse in reverse order
        for i in range(n-1,-1,-1) :
            #not ans because last element of arr is always leader
            #For rest of the elements, we are checking is it >=ans[-1] 
            if not ans or arr[i]>=ans[-1] : ans.append(arr[i])
        #Reverse the ans
        ans.reverse()
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna