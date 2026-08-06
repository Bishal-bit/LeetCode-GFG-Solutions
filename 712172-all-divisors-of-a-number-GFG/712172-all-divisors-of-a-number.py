class Solution:
    def getDivisors(self, n):
        # code here
        ans=[]
        i=1
        while i*i<=n :
            if n%i==0 :
                ans.append(i)
                if i!=n//i : ans.append(n//i)
            i+=1
        return sorted(ans)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna