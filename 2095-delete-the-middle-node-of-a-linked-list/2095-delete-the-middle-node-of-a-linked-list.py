# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next : return None
        #Go similer to cycle detection algorithm of LL to find the middle node
        slow=fast=head
        while fast and fast.next :
            #Use temp to eventually store node situated just before middle node
            temp=slow
            slow=slow.next
            fast=fast.next.next
            if slow==fast : break
        #Connect temp.next to temp.next.next That means slow i.e. middle node is removed
        temp.next=temp.next.next
        return head

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna