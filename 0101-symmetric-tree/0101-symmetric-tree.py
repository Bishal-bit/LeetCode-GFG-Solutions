# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def func(self, node1: TreeNode, node2: TreeNode ) :
        #If anyone is NULL then return node1==node2
        if not node1 or not node2 : return node1==node2

        #Compare node.val of both nodes. If not equal then return False
        if node1.val!=node2.val: return False
        
        #Compare node1's left child with node2's right child and vice-versa
        return self.func(node1.left, node2.right) and self.func(node1.right, node2.left)

    def isSymmetric(self, root: TreeNode | None) -> bool:
        return self.func(root.left, root.right)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna