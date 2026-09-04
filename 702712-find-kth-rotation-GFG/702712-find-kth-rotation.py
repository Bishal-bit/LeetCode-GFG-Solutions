class Solution:
    def findKRotation(self, arr):
        # code here
        n=len(arr)
        mini=float('inf')
        index=-1
        left, right=0, n-1
        while left<= right :
            mid=left+ (right-left)//2
            #If whole list is sorted left---mid---right
            #If arr[left]< mini, update mini and break
            if arr[left]<= arr[right] : 
                if arr[left]< mini :
                    mini=arr[left]
                    index=left
                break
        
            #if left---mid portion is sorted
            #if arr[left]< mini, update mini  
            #check for right portion by updating left
            elif arr[left]<= arr[mid] :
                if arr[left]< mini :
                    mini=arr[left]
                    index=left
                left=mid+1
        
            #if mid---right portion is sorted
            #if arr[mid]<mini, update mini 
            #check for left portion by updating right
            else:
                if arr[mid]<mini :
                    mini=arr[mid]
                    index=mid
                right=mid-1
        #Return index
        return index   

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna