# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None : return head
        #Declare odd,even, oddhead,evenhead
        odd=oddhead=head
        even=evenhead=head.next
        #Condition must be on even and evenhead
        while even and even.next :
            #Go for 2 steps for both odd,even
            odd.next=odd.next.next
            even.next=even.next.next
            #Shift odd, even
            odd=odd.next
            even=even.next
        #Connect odd index's last node to evenhead
        odd.next=evenhead
        #Return oddhead
        return oddhead
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna