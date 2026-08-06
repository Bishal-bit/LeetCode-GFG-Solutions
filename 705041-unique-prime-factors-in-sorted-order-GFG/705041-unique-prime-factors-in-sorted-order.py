class Solution:
    def primeFac(self, n):
        # code here
        #Go for traditional approach : Learnt during school days
        ans=[]
        i=2
        while i*i<=n :
            if n%i==0 : 
                ans.append(i)
                while n%i==0 : n//=i
            i+=1
        if(n>1) : ans.append(n)
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna