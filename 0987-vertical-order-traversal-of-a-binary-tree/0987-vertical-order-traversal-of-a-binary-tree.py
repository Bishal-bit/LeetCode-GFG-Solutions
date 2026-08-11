# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import defaultdict
    def dfs(self, node: Optional[TreeNode], row: int, col: int, mp) :
        if not node : return
        #Store row and node value for current column
        mp[col].append((row, node.val))
        #Left child -> row+1, col-1
        #Right child -> row+1, col+1
        self.dfs(node.left, row+1, col-1, mp)
        self.dfs(node.right, row+1, col+1, mp)

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        mp=defaultdict(list)
        self.dfs(root,0,0,mp)
        ans=[]
        #Traverse columns from left to right
        for col in sorted(mp) :
            #Sort by row then by value
            mp[col].sort()
            temp=[]
            #Take only node.val
            for row, val in mp[col] :
                #Append val to temp
                temp.append(val)
            #Append temp to ans
            ans.append(temp)
        #Return ans
        return ans


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna