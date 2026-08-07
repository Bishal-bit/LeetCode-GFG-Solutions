class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        #Sliding Window
        n=len(s)
        #Declare a map mp to record frequency of a,b,c
        mp={ 'a':0, 'b':0, 'c':0 }
        left= 0
        ans=0
        for right in range(n) :
            #Update mp[s[right]]
            mp[s[right]]+=1
            #If frequency of a,b,c is more than 0 then update ans as ans+=n-right, shrink window from left side
            while mp['a']>0 and mp['b']>0 and mp['c']>0 :
                ans+=n-right
                mp[s[left]]-=1
                left+=1
        #Return ans
        return ans


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna