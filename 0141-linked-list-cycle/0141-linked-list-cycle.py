# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #Declare 2 nodes as slow, fast
        slow=fast=head
        #Condition must be on fast as it's movement is more
        while fast and fast.next :
            #Slow single step, Fast double step
            slow=slow.next
            fast=fast.next.next
            #If slow==fast then loop exists.
            if slow==fast : return True
        return False
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna