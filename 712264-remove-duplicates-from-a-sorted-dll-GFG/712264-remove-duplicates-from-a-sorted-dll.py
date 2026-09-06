# class Node:
#     def __init__(self, value):
#         self.data = value  # value stored in node
#         self.next = None
#         self.prev = None

class Solution:
    def removeDuplicates(self, headRef):
        # code here
       temp=headRef
       
       while temp and temp.next:
           if temp.data==temp.next.data :
               dupli=temp.next
               temp.next=dupli.next
               if dupli.next : dupli.next.prev=temp
           else : temp=temp.next
       return headRef
               

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna