class Solution:
    def first1(self, arr, target) :
        n=len(arr)
        left, right=0, n-1
        ans=-1
        while left<= right :
            mid=left+ (right-left)//2
            if arr[mid]==target :
                #Update ans and check for left side portion by updating right
                ans=mid
                right=mid-1
            elif arr[mid]<target : left=mid+1
            else : right=mid-1
        return ans

    def last1(self, arr, target) :
        n=len(arr)
        left, right=0, n-1
        ans=-1
        while left<= right :
            mid=left+ (right-left)//2
            if arr[mid]==target :
                #Update ans and check for right side portion by updating left
                ans=mid
                left=mid+1
            elif arr[mid]<target : left=mid+1
            else : right=mid-1
        return ans
        
    def countFreq(self, arr, target):
        # code here
        a=self.first1(arr, target)
        #If first index is not found then no need to find the second index
        if a==-1 : return 0
        b=self.last1(arr, target)
        return b-a+1    #a...b

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna