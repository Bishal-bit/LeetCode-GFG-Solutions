# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #Declare temp1, temp2
        temp1, temp2=l1, l2
        dummy=dummyhead=ListNode(-1)
        carry=0
        while temp1 or temp2 :
            #if temp1 or temp2 is present then add val to carry and move both temp1 or temp2 by single step
            if temp1 : 
                carry+=temp1.val
                temp1=temp1.next
            if temp2 : 
                carry+=temp2.val
                temp2=temp2.next
            
            #Add carry%2 as next new node to dummy, carry//=10, shift dummy
            dummy.next=ListNode (carry%10)
            carry//=10
            dummy=dummy.next
        
        #If carry remains then add as mext node
        if carry : dummy.next=ListNode (carry)
        #Return dummyhead.next
        return dummyhead.next



        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna