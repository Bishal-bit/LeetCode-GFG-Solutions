class Solution:
    def func(self, i: int, k: int, target: int, v: List[int], ans :List[List[int]]) :
        
        if target==0 and len(v)==k : 
            ans.append(v.copy())
            return
        
        if target<0 or len(v)>k : return
        
        for it in range(i,10) :
            v.append(it)
            self.func(it+1, k, target-it, v, ans)
            v.pop()

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        self.func(1, k, n, [], ans)
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna