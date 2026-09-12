'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def isleaf(self, node) :
        #Checking if node is leaf node or not
        if not node.left and not node.right : return True
        return False
    
    def leftboundary(self, node, ans) :
        #Pushing all left boundary nodes
        while node :
            if  not self.isleaf(node) : ans.append(node.data)
            #You have to check for both left & right children
            if node.left : node=node.left
            else : node=node.right

    def inorder(self, node, ans) :
        if not node : return
        if self.isleaf(node) : ans.append(node.data)
        if node.left : self.inorder(node.left, ans)
        if node.right : self.inorder(node.right, ans)
        
    def rightboundary(self, node, ans) :
        #Pushing all right boundary nodes
        ans1=[]
        while node :
            if  not self.isleaf(node) : ans1.append(node.data)
            #You have to check for both right & left children
            if node.right : node=node.right
            else : node=node.left
        #Node wise right boundary is in reverse order
        for i in range(len(ans1)-1, -1, -1) :
            ans.append(ans1[i])
    
    def boundaryTraversal(self, root):
        # code here
        ans=[]
        if not root : return ans
        #Check root node is a leaf node or not
        if  not self.isleaf(root) : ans.append(root.data)
        #Left boundary
        self.leftboundary(root.left, ans)
        #Inorder
        self.inorder(root, ans)
        #Right boundary
        self.rightboundary(root.right, ans)
        return ans
        
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna