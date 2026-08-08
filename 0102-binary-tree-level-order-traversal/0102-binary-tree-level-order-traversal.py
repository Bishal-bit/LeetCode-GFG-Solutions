# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        if not root : return ans
        #Dequeue is used for FIFO
        q=deque()
        #Append root node inside q
        q.append(root)

        while q :
            level=[]        #level for storing node.vals of each level
            n=len(q)
            #There would be multiple nodes inside queue
            #That's why for loop is used
            for i in range(n) :
                node=q.popleft()    #Access node that pushed first
                
                #Append node.val to level then check for left,right
                level.append(node.val)
                if node.left : q.append(node.left)
                if node.right : q.append(node.right)
            #Append level t ans
            ans.append(level)
        
        #Return ans
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna