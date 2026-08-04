# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Declare dummy node as there are chances to be asked to delete 1st node
        dummy=ListNode(0)
        dummy.next=head
        #Declare slow, fast
        slow=fast=dummy


        #Go upto n for fast node
        for i in range(n+1) :
            fast=fast.next
        
        #Now both go for L-n
        while fast :
            slow=slow.next
            fast=fast.next
        
        #Slow's next node is the one to be deleted
        slow.next=slow.next.next
        #Return dummy.next
        return dummy.next


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna