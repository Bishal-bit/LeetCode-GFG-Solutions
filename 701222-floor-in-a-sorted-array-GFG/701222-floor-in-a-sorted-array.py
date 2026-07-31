class Solution:
    def findFloor(self, arr, x):
        # code here
        n=len(arr)
        low, high=0, n-1
        #Initialize ans as n in case no element is greater than target
        ans=-1
        while low<=high :
            #Calculate mid
            mid=low + (high-low)//2
            #If arr[mid]>=x then update ans as mid and check the left portion by high=mid-1
            if arr[mid]<=x :
                ans=mid
                low=mid+1
            #Else update low as mid+1
            else : 
                high=mid-1
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna