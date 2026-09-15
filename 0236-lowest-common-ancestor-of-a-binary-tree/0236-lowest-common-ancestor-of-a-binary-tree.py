# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root==p or root==q : return root
        left1=self.lowestCommonAncestor(root.left, p, q)
        right1=self.lowestCommonAncestor(root.right, p, q)
        #They are on different subtrees return not NULL node
        if not left1 : return right1
        elif not right1 : return left1
        #They are on same subtree, LCS is found
        return root

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna