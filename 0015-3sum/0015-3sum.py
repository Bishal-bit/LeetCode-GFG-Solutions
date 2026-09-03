class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)
        #Reminder: Must sort the given list to apply search operation
        nums.sort()
        ans=[]
        for i in range(n) :
            #Here we are skipping duplicates 
            #nums[i] can not contain same value for different triplets
            if i>0 and nums[i]==nums[i-1] : continue
            j, k=i+1, n-1
            while j<k :
                total=nums[i] + nums[j] + nums[k]
                #total>0 then decrease k
                if total>0 : k-=1
                #total<0 then increase j
                elif total<0 : j+=1
                #If total==0 then push increase j, decrease k
                else : 
                    ans.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    #Here we are skipping duplicates 
                    #nums[j],nums[k] can not contain same value for different triplets
                    while j<k and nums[j]==nums[j-1] : j+=1
                    while j<k and nums[k]==nums[k+1] : k-=1
        return ans


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna