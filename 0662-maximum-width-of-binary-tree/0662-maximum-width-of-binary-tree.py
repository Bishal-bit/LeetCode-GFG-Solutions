# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #We have to go for Level order traversing. Queue is required
        if not root : return 0
        maxi=0
        #Declare q
        q=deque()
        #Append (root,0) to q
        q.append((root,0))
        while q :
            #mini will be used to always start index from 0 to get rid of overflow of index
            mini=q[0][1]
            n=len(q)        #No of nodes at each level
            start=end=0
            for i in range(n) :
                node, index=q.popleft()
                index-=mini
                #Start---end for each level
                if i==0 : start=index
                if i==n-1 : end=index
                #For left node index value would be 2*index+1
                #For right node index value would be 2*index+2
                if node.left : q.append((node.left, 2* index +1))
                if node.right : q.append((node.right, 2* index +2))
            #Update maxi
            maxi=max(maxi, end-start+1)
        return maxi
            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna