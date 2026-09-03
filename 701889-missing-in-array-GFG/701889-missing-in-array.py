class Solution:
    def missingNum(self, arr):
        # code here
        #Use exor operation
        n=len(arr)
        exor1=exor2=0
        for i in range(n) :
            #exor1 is acountable for i from 0 to (n-1)
            #exor2 is acountable for arr[i] from 0 to arr[n-1]
            exor1^=i
            exor2^=arr[i]
        #exor1 is acountable for n and n+1
        exor1^=n
        exor1^=n+1
        #Return exor1^exor2
        return exor1^exor2

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna