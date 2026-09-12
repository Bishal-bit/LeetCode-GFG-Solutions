# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #If out of p, q anyone is None then return p==q
        if not p or not q : return p==q
        #If val of p, q are different then return False
        if p.val!=q.val : return False
        #Return left side for p,q and right side for p,q
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna