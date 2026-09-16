'''
Definition for Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None 
'''
        
class Solution:
    def findCeil(self,root, x):
        # code here
        ans=-1
        while root :
            #If x is to be found as root.data then ans=root.data
            if root.data==x : 
                ans=root.data
                break
            #If x<root.data : store root.data as ans then go left
            #Else go right
            elif x<root.data :
                ans=root.data
                root=root.left
            else : root=root.right
        #Return ans
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna