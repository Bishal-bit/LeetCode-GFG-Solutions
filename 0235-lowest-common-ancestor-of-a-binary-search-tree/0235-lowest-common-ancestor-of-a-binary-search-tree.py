# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root :
            #If p,q are greater than root.val then go for right
            if root.val<p.val and root.val<q.val : root=root.right
            #If p,q are less than root.val then go for left child
            elif p.val<root.val and q.val<root.val : root=root.left
            #Return root
            else : return root

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna