# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root: Optional[TreeNode], ans: List[int]) :
        #If root==NULL then just return
        #root->left->right
        if not root : return
        ans.append(root.val)
        self.dfs(root.left,ans)
        self.dfs(root.right,ans)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        #DFS Traversal
        self.dfs(root,ans)
        #Return ans
        return ans

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
