class Solution:
    def func(self,index :int,candidates: List[int], target: int,n: int,v : List[int],ans :List[List[int]]) :
        #Use index, target if condition separately to get rid of index out of bound error
        if index==n :
            if target==0 : 
                #We want stored ans to be unchanged that is why used v.copy()
                ans.append(v.copy())
            return
        
        if candidates[index]<=target :
            v.append(candidates[index])
            self.func(index, candidates, target-candidates[index], n, v, ans)
            v.pop()     #v.pop() for backtracking
        #Go for next index
        self.func(index+1, candidates, target, n, v, ans)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        ans=[]
        self.func(0, candidates, target, n, [], ans)
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna