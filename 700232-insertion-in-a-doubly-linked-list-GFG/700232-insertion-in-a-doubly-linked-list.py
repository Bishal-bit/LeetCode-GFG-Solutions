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
        count=0
        temp=head
        while temp :
            #count==p is for finding out the position be shifting temp
            if count==p : break
            temp=temp.next
            count+=1
        #If p crossed whole doubly LL then just return head
        if temp is None : return head
        
        
        #Declare newNode
        newNode=Node(x)
        #Declare temp1
        temp1=temp.next
        #Connect newNode's prev and next 
        newNode.next=temp1
        newNode.prev=temp
        
        
        #If temp is the last node then temp1 is actually NULL
        #So check if it actually exists or not
        #Based on this connect prev,next pointing to newNode
        if temp1 : temp1.prev=newNode
        temp.next=newNode
        #Return head
        return head
        
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna