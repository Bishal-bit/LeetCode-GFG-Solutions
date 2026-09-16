# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, node: TreeNode) :
        if not node : return
        #Go for node.left recursion
        self.inorder(node.left)
        #Rather than storing to array Do decrement self.k
        #If not self.k then node.val is our ans
        self.k-=1
        if not self.k : 
            self.ans=node.val
            return
        #Go for root.right recursion
        self.inorder(node.right)
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        #Go for Inorder traversal as inorder of BST gives sorted array
        self.ans=-1
        self.k=k
        self.inorder(root)
        return self.ans
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna