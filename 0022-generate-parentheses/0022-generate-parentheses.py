class Solution:
    def func(self,open: int,close: int,n: int,s: str,ans :list[str]) :
        #Condition meet then push string s to ans
        if open==close and open+close==2*n : ans.append(s)
        #If(open<n) increse open parentheses
        if open<n : self.func(open+1,close,n, s+"(",ans)
        #If(close<open) increse close parentheses
        if close<open : self.func(open,close+1,n, s+")",ans)
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        open, close=0, 0
        self.func(open,close,n, "",ans)
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna