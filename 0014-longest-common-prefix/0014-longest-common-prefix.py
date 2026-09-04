class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs : return ""
        pre=strs[0]
        n=len(pre)
        #Traverse through characters of pre i.e. 1st string
        for i in range(n) :
            #Strore character to ch
            ch=pre[i]
            #Traverse through other strings of list
            #Match character by character
            #If mismatch happens then return substring
            for word in strs[1:] :
                if i==len(word) or ch!=word[i] : return pre[:i]
        #If no mismatch then return whole string of pre
        return pre

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna