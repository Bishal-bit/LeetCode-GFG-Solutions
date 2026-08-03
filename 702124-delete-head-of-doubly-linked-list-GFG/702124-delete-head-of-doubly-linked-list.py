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
        #If it is only a single node then return None
        if head.next is None : return None
        #Declare temp as head.next
        #Disconnect head and temp
        temp=head.next
        temp.prev=None
        head.next=None
        #Return temp
        return temp
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna