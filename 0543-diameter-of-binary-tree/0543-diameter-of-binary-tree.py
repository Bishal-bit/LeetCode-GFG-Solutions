# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def func(self, root: Optional[TreeNode]) ->int:
        if root is None : return 0
        l=self.func(root.left)
        r=self.func(root.right)
        #Update self.diam
        self.diam=max(self.diam, l+r)
        return 1+max(l,r)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #self.diam is similer to pass by reference 
        self.diam=0
        self.func(root)
        return self.diam

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna