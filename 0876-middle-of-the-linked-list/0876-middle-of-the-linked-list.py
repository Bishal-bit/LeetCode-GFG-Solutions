# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Declare 2 nodes as slow, fast
        slow=fast=head
        #Condition must be on fast as we will adjust mid pision based on this condition
        while fast and fast.next :
            #Slow single step, Fast double step
            slow=slow.next
            fast=fast.next.next
        #Slow is at mid position
        return slow

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna