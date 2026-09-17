'''
Structure of a Binary Search Tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    def func(self, node, key) :
        #Inorder traversal, to get sorted nodes.
        if not node : return
        self.func(node.left, key)
        #If node.data<key update at same index so that we get the last smallest element than k.
        if node.data<key : self.ans[0]=node
        #If node.data>key and self.ans[1] is None then update & it's done for bigger element.
        if node.data>key and self.ans[1] is None: self.ans[1]=node
        self.func(node.right, key)
        
    def findPreSuc(self, root, key):
        # code here
        self.ans=[None, None]
        self.func(root,key)
        return self.ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna