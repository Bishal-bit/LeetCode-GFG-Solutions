"""
Definition of Node
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def func(self, node, path, ans) :
        if not node : return
        #Push each node.data to path
        path.append(node.data)
        #If we are at leaf node then push path to ans
        #Else go for left and right child
        if not node.left and not node.right : ans.append(path.copy()) #Use .copy() for path
        else :
            if node.left : self.func(node.left, path, ans)
            if node.right : self.func(node.right, path, ans)
        #Don't forget to use pop_back() for path
        #It will pop out the last element from path so that
        #we can explore other root to leaf paths
        path.pop()
    
    
    def paths(self, root):
        # code here
        path=[]
        ans=[]
        self.func(root, path, ans)
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna