# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Do same as finding middle of LL
        if head==None or head.next==None : return None
        slow=fast=head
        while fast and fast.next :
            #Use temp to eventually store node situated just before middle node
            temp=slow
            slow=slow.next
            fast=fast.next.next
        
        #Connect temp.next to slow.next That means slow node is removed
        temp.next=slow.next
        return head

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna