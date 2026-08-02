class Solution:
    def nthRoot(self, n, m):
       # code here
       left, right=0, m
       while left<=right :
           mid=left+ (right-left)//2
           val=mid**n
           if val==m : return mid
           elif val<m : left=mid+1
           else : right=mid-1
       return -1


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna