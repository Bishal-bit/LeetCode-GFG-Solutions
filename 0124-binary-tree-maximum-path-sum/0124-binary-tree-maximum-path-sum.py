# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def func(self, node: Optional[TreeNode]) :
        #If node is None then return 0
        if not node : return 0
        #For l,r we have to count only (+)ve node.val so max(0,...) is used
        l=max(0, self.func(node.left))
        r=max(0, self.func(node.right))
        #Count maxsum and update it to self.maxsum
        maxsum=node.val+l+r
        self.maxsum=max(self.maxsum,maxsum)
        #Return node.val+max(l,r)
        return node.val+max(l,r)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #Initialize self.maxsum as -inf
        self.maxsum=float('-inf')
        self.func(root)
        #Return self.maxsum
        return self.maxsum

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna