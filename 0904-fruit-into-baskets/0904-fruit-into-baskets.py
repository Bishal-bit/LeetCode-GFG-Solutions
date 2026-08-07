class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #Sliding Window
        n=len(fruits)
        mp={}
        left, right=0, 0
        ans=0
        while right<n :
            #Pass elements to the map mp
            mp[fruits[right]]=mp.get(fruits[right],0)+1
            #If len(mp) exceeds 2 then, decrement mp[fruits[left]]
            #                          ,if mp[fruits[left]]==0 then pop it
            #                          ,increment left
            if len(mp)>2 :
                mp[fruits[left]]-=1
                if mp[fruits[left]]==0 : mp.pop(fruits[left])
                left+=1
            #Update ans, increment right
            ans=max(ans,right-left+1)
            right+=1
        #Return ans
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna