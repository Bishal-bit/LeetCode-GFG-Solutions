# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def func(self, node: TreeNode, level: int, ans: List[int]) :
        if not node : return
        #level==ans.size() is true only when for each level, we meet the right most node
        if len(ans)==level : ans.append(node.val)
        #We want right side view so 1st check right node then left node
        #For each func() increment level
        if node.right : self.func(node.right, level+1, ans)
        if node.left : self.func(node.left, level+1, ans)

    def rightSideView(self, root: TreeNode | None) -> list[int]:
        ans=[]
        self.func(root, 0, ans)
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna