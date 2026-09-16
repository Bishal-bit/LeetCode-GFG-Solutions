# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node : TreeNode) :
        #If left child is NULL return right child and vice-versa
        if not node.left : return node.right
        if not node.right : return node.left
        #Store left and right children of node, which is to be deleted
        left1, right1=node.left, node.right
        #From left child go for it's right most child
        #Connect right1 as it's right child
        current=left1
        while current.right :
            current=current.right
        current.right=right1
        #Return left1
        return left1
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if not root : return root
        node=root
        while node :
            #If node.val is the key then direct return helper()
            if node.val==key : return self.helper(node)
            #if node.val<key then go for rightchild
            if node.val<key : 
                #If right child exists & is the key then go for helper()
                #Else simply node=node.right
                if node.right and node.right.val==key : node.right=self.helper(node.right)
                else : node=node.right
            #if node.val>key then go for leftchild
            else :
                #If left child exists & is the key then go for helper()
                #Else simply node=node.left
                if node.left and node.left.val==key : node.left=self.helper(node.left)
                else : node=node.left
        return root

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna