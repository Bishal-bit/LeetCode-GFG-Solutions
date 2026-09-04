class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t={}
        t_to_s={}
        #Iterate through both by using zip()
        for a,b in zip(s, t) :
            #If a is in map s_to_t and any mismatch happens return False
            #If b is in map t_to_s and any mismatch happens return False
            if a in s_to_t and s_to_t[a]!=b : return False
            if b in t_to_s and t_to_s[b]!=a : return False

            #Store a, b to maps s_to_t and t_to_s
            s_to_t[a]=b
            t_to_s[b]=a
        
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna