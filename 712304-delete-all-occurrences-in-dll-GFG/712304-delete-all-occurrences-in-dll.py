"""
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

"""
class Solution:
    
    # Function to delete all occurrences of x
    def deleteAllOccurOfX(self, head, x):
        # code here
        temp=head
        while temp :
            #Store next node of temp as nex
            nex=temp.next
            if temp.data==x :
                #If not temp.prev then shift head
                #Else temp.prev.next=temp.next
                if not temp.prev : head=temp.next
                else : temp.prev.next=temp.next
                
                #If temp.next then temp.next.prev=temp.prev
                if temp.next : temp.next.prev=temp.prev
            #Update temp
            temp=nex
        return head
                

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna