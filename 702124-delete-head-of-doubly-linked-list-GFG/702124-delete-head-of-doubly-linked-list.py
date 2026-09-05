''' Structure of doubly linked list Node
 class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.prev = None
'''
class Solution:
    def deleteHead(self, head):
        # code here
        #If it is empty or only a single node then return None
        if not head or not head.next : return None
        #Shift head to head.next and do head.prev=None
        head=head.next
        head.prev=None
        
        #Return head
        return head
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna