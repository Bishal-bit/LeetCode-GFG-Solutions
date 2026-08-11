# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #It is almost same as level order traversal
        ans=[]
        if not root : return ans
        #Declare a queue and flag
        q=deque([root])
        flag=True
        while q :
            n=len(q)
            level=[]
            for i in range(n) :
                #Pop node from q and append it's val to level
                node=q.popleft()
                level.append(node.val)
                #Check for node.left and node.right
                if node.left : q.append(node.left)
                if node.right : q.append(node.right)
            #Based on flag do reverse operation
            if not flag : level.reverse()
            #Append level to ans and change flag
            ans.append(level)
            flag=not flag
        #Return ans
        return ans
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna