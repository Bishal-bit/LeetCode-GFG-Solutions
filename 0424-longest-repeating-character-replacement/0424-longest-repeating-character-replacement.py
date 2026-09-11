class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        mp={}
        left=right=0
        #freq is for storing the character having highest frequency
        freq=maxi=0
        while right< n :
            #Update mp[s[right]] based on frequency 
            mp[s[right]]=mp.get(s[right],0)+1
            #Update freq
            freq=max(freq,mp[s[right]])
            #If (right-left+1)-freq exceeds k then decrement mp[s[left]],increment left
            if (right-left+1)-freq > k :
                mp[s[left]]-=1
                left+=1
            #Update maxi, increment right
            maxi=max(maxi, right-left+1)
            right+=1
        #Return maxi
        return maxi


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna