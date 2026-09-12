# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def func(self, node: Optional[TreeNode], ans: List[int]) :
        #If node is None then just return
        if not node : return

        #Node.left-->Node.right-->Node.val
        self.func(node.left, ans)
        self.func(node.right, ans)
        ans.append(node.val)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        self.func(root, ans)
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna