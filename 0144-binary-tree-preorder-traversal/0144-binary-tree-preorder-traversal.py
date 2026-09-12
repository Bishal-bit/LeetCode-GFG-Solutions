# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def func(self, node: Optional[TreeNode], ans: List[int]) :
        #If it is None node then just return
        if not node : return 
        
        #Node.val-->Node.left-->Node.right
        ans.append(node.val)
        self.func(node.left, ans)
        self.func(node.right, ans)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        self.func(root, ans)
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna