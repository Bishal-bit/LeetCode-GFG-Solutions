# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def func(self, node: TreeNode, lb: int, hb: int) :
        if not node or self.ans==False : return
        #If node.val goes out of bound then self.ans=False & return
        if node.val<=lb or node.val>=hb : 
            self.ans=False
            return
        #If we go for left child then left child's val should be < node.val
        if node.left : self.func(node.left, lb, node.val)
        #If we go for right child then right child's val should be > node.val
        if node.right : self.func(node.right, node.val, hb)
    def isValidBST(self, root: TreeNode | None) -> bool:
        self.ans=True
        #lower bound=float('-inf'), higher bound=float('inf')
        self.func(root, float('-inf'), float('inf'))
        return self.ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna