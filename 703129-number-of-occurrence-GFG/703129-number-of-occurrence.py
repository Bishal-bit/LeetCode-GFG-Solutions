class Solution:
    def first1(self, arr, target, n) -> int :
        first=-1
        left, right=0, n-1
        while left<=right :
            mid=left+ (right-left)//2
            if arr[mid]==target :
                #Update first and check for left side portion by updating right
                first=mid
                right=mid-1
            elif arr[mid]<target : left=mid+1
            else : right=mid-1
        return first

    def last1(self, arr, target, n) -> int :
        last=-1
        left, right=0, n-1
        while left<=right :
            mid=left+ (right-left)//2
            if arr[mid]==target :
                #Update last and check for right side portion by updating left
                last=mid
                left=mid+1
            elif arr[mid]<target : left=mid+1
            else : right=mid-1
        return last
    def countFreq(self, arr, target):
        # code here
        n=len(arr)
        a=self.first1(arr,target,n)
        #If first index is not found then no need to find the second index
        if a==-1 : return 0
        b=self.last1(arr,target,n)
        return b-a+1
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna