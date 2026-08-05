# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #Declare temp1, temp2
        temp1, temp2=headA, headB
        while(temp1 !=temp2) :
            #Move both temp1, temp2 by single step
            temp1=temp1.next
            temp2=temp2.next
            #If temp1==temp2 then return temp1
            if temp1==temp2 : return temp1

            #If temp1 reaches to None then reinitialize it to headB
            #If temp2 reaches to None then reinitialize it to headA
            if temp1==None : temp1=headB
            if temp2==None :temp2=headA
        
        #Return temp1
        return temp1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna