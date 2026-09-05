''' Structure of linked list Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def getCount(self, head):
        # code here
        temp=head
        #If it's empty return 0 
        if not temp : return 0
        count=0
        #Count no of nodes by traversing nodes of linkedlist
        while temp :
            count+=1
            temp=temp.next
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna