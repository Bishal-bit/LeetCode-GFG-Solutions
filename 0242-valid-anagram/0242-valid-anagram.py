class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ns, nt=len(s), len(t)

        #If strings having different length then return False
        if ns!=nt : return False

        #Declare list as we will deal based on ASCII values
        freq=[0]*26
        for i in range(ns) :
            #ord() is for ASCII values of characters
            freq[ord(s[i])-ord('a')]+=1
            freq[ord(t[i])-ord('a')]-=1
        
        #If any element of freq is not 0 then return False
        for it in freq :
            if it!=0 : return False
        
        #Return True
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna