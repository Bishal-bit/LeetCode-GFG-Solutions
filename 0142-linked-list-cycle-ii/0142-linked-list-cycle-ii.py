# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=fast=head
        #Go similer to cycle detection algorithm of LL
        while fast and fast.next :
            slow=slow.next
            fast=fast.next.next
            #If slow==fast i.e. cycle detected then break
            if slow==fast : break
        #Else executes when the loop finishes normally i.e. it was not stopped by break
        else : return None      #If there is no loop
        #Slow is reinitialized as head
        slow=head
        #Go for single movement of both slow, fast untill they meet
        while slow!=fast :
            slow=slow.next
            fast=fast.next
        #Return slow
        return slow

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna