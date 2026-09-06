''' structure of linked list Node
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def func(self, temp) :
        #Backtracking
        if not temp : return 1      #Base case
        carry=self.func(temp.next)
        temp.data+=carry
        if temp.data<10 : return 0
        else :
            temp.data=0
            return 1
    
    def addOne(self,head):
        # code here
        #return head of list after adding one
        carry=self.func(head)
        if carry :
            newnode=Node(1)
            newnode.next=head
            return newnode
        return head

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna