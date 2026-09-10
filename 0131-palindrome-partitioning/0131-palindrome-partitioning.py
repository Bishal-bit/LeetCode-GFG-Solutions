class Solution:
    def palindrome(self, s: str, start: int, end: int)->bool :
        #Check if substring is palindrome or not
        while start<= end :
            if s[start]!=s[end] : return False
            start+=1
            end-=1
        return True
    def func(self, index: int, s: str, n: int, path: List[int], ans: List[List[str]]) :
        if index==n :
            ans.append(path.copy())
            return
        for i in range(index,n) :
            if self.palindrome(s, index, i) :
                #If substring is palindrome then append it to path
                path.append(s[index:i+1])
                #Explore more
                self.func(i+1, s, n,path, ans)
                #Undo it
                path.pop()
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        path=[]
        ans=[]
        self.func(0, s, n,path, ans)
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna