class Solution:
    def subsets(self, arr):
        # code here
        n=len(arr)
        ans=[]
        for i in range(1<<n) :      #(1<<n) = 2^n
            subset=[]
            for j in range(n) :
                if i & (1<<j) :
                    subset.append(arr[j])
            ans.append(subset)
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna