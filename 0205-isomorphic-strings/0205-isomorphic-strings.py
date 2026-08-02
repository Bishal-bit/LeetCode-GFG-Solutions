class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #Declare 2 maps
        mapst={}
        mapts={}
        #Iterate through both
        for i,j in zip(s,t) :
            #If element is in map then check if there is any mismatch
            if i in mapst :
                if mapst[i]!=j : return False
            #Else add it in map
            else : mapst[i]=j
            #If element is in map then check if there is any mismatch
            if j in mapts :
                if mapts[j]!=i : return False
            #Else add it in map
            else : mapts[j]=i
        #No mismatch. So return True
        return True
                


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna