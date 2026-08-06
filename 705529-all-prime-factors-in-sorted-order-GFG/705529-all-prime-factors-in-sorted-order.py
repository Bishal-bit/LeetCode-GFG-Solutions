class Solution:
    def printPrimeFactorization(self, n):
        #code here
        ans=[]
        i=2
        while i*i<=n :
            while n%i==0 : 
                ans.append(i)
                n//=i
            i+=1
        if n>1 : ans.append(n)
        # * is unpacking operator
        print(*ans, end="")

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna