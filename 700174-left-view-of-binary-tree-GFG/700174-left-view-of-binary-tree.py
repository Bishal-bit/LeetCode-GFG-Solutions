''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None 
'''

class Solution:
    def func(self, node, level, ans) :
        if not node : return
        #level==ans.size() is true only when for each level, we meet the left most node
        if len(ans)==level : ans.append(node.data)
        #We want left side view so 1st check left node then right node
        #For each func() increment level
        if node.left : self.func(node.left, level+1, ans)
        if node.right : self.func(node.right, level+1, ans)
    def leftView(self, root):
        # code here
        ans=[]
        self.func(root, 0, ans)
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna