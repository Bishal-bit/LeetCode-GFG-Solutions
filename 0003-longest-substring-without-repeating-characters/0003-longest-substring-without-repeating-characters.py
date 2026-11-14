class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Sliding Window
        n=len(s)
        if n==0 : return 0
        left=0
        st=set()            #Declare set()
        ans=float('-inf')
        for right in range(n) :
            #If s[right] is already there in set then we have to shrink from left side for the purpose of removing it
            while s[right] in st :
                st.remove(s[left])
                left+=1
            #Add s[right] to the set and update ans
            st.add(s[right])
            ans=max(ans, right-left+1)
        ##Return ans
        return ans


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna