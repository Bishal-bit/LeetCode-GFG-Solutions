class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Sliding Window
        n=len(s)
        st=set()            #Declare set()
        maxi=0
        left, right=0, 0
        for right in range(n) :
            #If s[right] is already there in set then we have to shrink from left side for the purpose of removing it
            while s[right] in st :
                st.remove(s[left])
                left+=1
            #Add s[right] to the set and update maxi
            st.add(s[right])
            maxi=max(maxi, right-left+1)
        #Return maxi
        return maxi


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna