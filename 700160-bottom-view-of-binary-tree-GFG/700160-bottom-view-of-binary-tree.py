'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def bottomView(self, root):
        # code here
        if not root : return
        q=deque()           #Node, vertical
        q.append([root, 0])
        mp={}               #{vertical,node->data}
        while q :
            node, val=q.popleft()
            #Update mp[val] as node.data
            mp[val]=node.data
            if node.left : q.append([node.left, val-1])
            if node.right : q.append([node.right, val+1])
        ans=[]
        for it in sorted(mp) :
            ans.append(mp[it])
        return ans  

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna