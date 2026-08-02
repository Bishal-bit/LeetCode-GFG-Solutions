class Solution:
    def frequencySort(self, s: str) -> str:
        #Declare a map to store elements of string along with their frequency
        mp={}
        #Pass elements of string along with their frequency
        for it in s :
            mp[it]=mp.get(it,0)+1
        #Sort based on value in descending order
        mp1=dict(sorted(mp.items(), key= lambda x : x[1], reverse=True))
        ans=[]
        #Store it to a new string ans
        for key,value in mp1.items() :
            ans.append(key*value)
        #"".join(ans) convers list to string
        return "".join(ans)
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna