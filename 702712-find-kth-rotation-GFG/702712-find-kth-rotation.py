class Solution:
    def findKRotation(self, arr):
        # code here
        n=len(arr)
        left, right=0, n-1
        #Initialize ans as -inf and index as None
        ans=float('inf')
        index=None
        while left<=right :
            mid=left+ (right-left)//2
            #If whole list is sorted left---mid---right
            #Update ans and index then break
            if arr[left]<arr[right] :
                if arr[left]<ans :
                    ans=arr[left]
                    index=left
                break
            #if left---mid portion is sorted
            #Update ans and index then check for right portion by updating left
            elif arr[left]<=arr[mid] :
                if arr[left]<ans :
                    ans=arr[left]
                    index=left
                left=mid+1
            #if mid---right portion is sorted
            #Update ans and index then check for left portion by updating right
            else :
                if arr[mid]<ans :
                    ans=arr[mid]
                    index=mid
                right=mid-1
        #Return index
        return index
                

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna