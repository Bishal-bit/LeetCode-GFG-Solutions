class Solution:
    def powerSet(self, s):
       #code here
       n=len(s)
       result=[]
       for i in range(1<<n) :
           subset=""
           for j in range(n) :
               if i & (1<<j) : subset+=s[j]
           result.append(subset)
       return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna