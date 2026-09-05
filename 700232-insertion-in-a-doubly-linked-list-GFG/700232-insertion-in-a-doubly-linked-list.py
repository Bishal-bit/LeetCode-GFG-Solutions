''' Structure of Doubly Linked List Node
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

'''

class Solution:
    def insertAtPos(self, head, p, x):
        # Code Here
        temp=head
        count=0
        while temp :
            #count==p is for finding out the position of insertion
            if count==p : break
            count+=1
            temp=temp.next
        #If p crossed whole doubly LL then just return head
        if not temp : return head
        
        #Declare newnode, temp1
        newnode=Node(x)
        temp1=temp.next
        #Connect newnode's prev and next 
        newnode.next=temp1
        newnode.prev=temp
        
        #If temp is the last node then temp1 is actually NULL
        #So check if it actually exists or not
        #Based on this connect prev,next pointing to newnode
        if temp1 : temp1.prev=newnode
        temp.next=newnode
        return head
        
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna