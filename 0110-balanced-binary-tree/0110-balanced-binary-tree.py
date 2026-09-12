# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def func(self, node: Optional[TreeNode])->int :
        if not node : return 0
        l=self.func(node.left)
        r=self.func(node.right)
        #Check for imbalance
        if l==-1 or r==-1 or abs(l-r)>1 : return -1
        return 1+ max(l, r)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #Use max depth algorithm of Binary tree 
        #If it is imbalanced then function returns -1
        return self.func(root)!=-1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna