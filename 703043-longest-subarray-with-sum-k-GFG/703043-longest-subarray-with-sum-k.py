class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        n=len(arr)
        presum={}
        sum=0
        maxlen=0
        for i in range(n) :
            #Calculate prefix sum
            sum+=arr[i]
            #If sum==k then update maxlen 
            if(sum==k) : maxlen=max(maxlen,i+1)
            #Count remain
            rem=sum-k
            #If rem is present in map then count length as i-presum[rem]
            #Update maxlen
            if rem in presum :
                length=i-presum[rem]
                maxlen=max(maxlen,length)
            #If sum is not there in map update it with index value
            if sum not in presum : 
                presum[sum]=i
        #Return maxlen
        return maxlen

    


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna