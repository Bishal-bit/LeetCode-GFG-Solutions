class Solution:
    def func(self,index :int,candidates: List[int], target: int,n: int,v : List[int],ans :List[List[int]]) :
        if target==0 :
            ans.append(v.copy())
            return
        #Use for loop
        for i in range(index,n) :
            #If same numerical no is repeated then skip them
            if i>index and candidates[i]==candidates[i-1] : continue
            if candidates[i]<=target :
                v.append(candidates[i])
                self.func(i+1, candidates, target-candidates[i], n, v, ans)
                v.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        #Sorting is must
        candidates.sort()
        ans=[]
        self.func(0, candidates, target, n, [], ans)
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna