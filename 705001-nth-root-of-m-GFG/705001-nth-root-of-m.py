class Solution:
    def nthRoot(self, n, m):
       # code here
       # From 0 we have to check to reach m
       left, right=0, m
       while left<= right :
           mid=left + (right-left)//2
           #Check for mid
           val=mid**n
           if val==m : return mid
           #If val<m the we have to increment so update left to shift towrds right portion
           elif val<m : left=mid+1
           #If val>m the we have to decrement so update right to shift towrds left portion
           else : right=mid-1
       #Return -1
       return -1


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna