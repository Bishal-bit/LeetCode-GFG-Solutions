# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        #If not root then return TreeNode(val)
        if not root : return TreeNode(val)
        node=root
        while node :
            #If node.val<val go for right node if it exists : otherwise attach new node to right
            if node.val< val : 
                if node.right : node=node.right
                else : 
                    node.right=TreeNode(val)
                    break
            #If val<node.val go for left node if it exists : otherwise attach new node to left
            else : 
                if node.left : node=node.left
                else : 
                    node.left=TreeNode(val)
                    break
        return root

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna