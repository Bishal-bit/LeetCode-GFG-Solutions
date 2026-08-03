""" Structure of Doubly Linked List Node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        # code here
        #If it is only a single node then return head
        if head is None or head.next is None : return head
        #Declare temp, pre
        temp=head
        pre=None
        while temp :
            pre=temp.prev
            temp.prev=temp.next
            temp.next=pre
            
            #Move to the next node. Here, temp.prev=temp.next
            temp=temp.prev
        #pre points to the previous node of new head
        #So head=pre.prev 
        if pre : head=pre.prev    
        return head
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna