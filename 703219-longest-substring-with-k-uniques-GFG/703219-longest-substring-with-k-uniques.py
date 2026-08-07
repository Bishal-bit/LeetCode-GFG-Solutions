class Solution:
    def longestKSubstr(self, s, k):
        # code here
        n=len(s)
        #Declare map mp to record characters
        mp={}
        left, right=0, 0
        ans=0
        while right < n :
            #Update mp[s[right]]
            mp[s[right]]=mp.get(s[right],0)+1
            #If no of distinct characters exceeds k then shrink window from left
            while len(mp)>k :
                mp[s[left]]-=1
                if mp[s[left]]==0 : mp.pop(s[left])
                left+=1
            #Update ans
            ans=max(ans,right-left+1)
            right+=1
        #Unable to get k distinct characters results -1
        if len(mp)< k : return -1
        return ans
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna