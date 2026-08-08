# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Using Stack
        ans=[]
        if not root : return ans
        st=[]
        st.append(root)
        while st :
            #Access top node, pop it then put it's value to ans
            node=st.pop()
            ans.append(node.val)
            #Due to LIFO nature of stack we push right then left
            #So that left comes out before right
            if node.right : st.append(node.right)
            if node.left : st.append(node.left)
        #Return ans
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna