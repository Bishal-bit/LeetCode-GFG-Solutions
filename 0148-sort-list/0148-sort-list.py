# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, ll1: Optional[ListNode], ll2: Optional[ListNode]) :
        temp1, temp2=ll1, ll2
        dummy=dummyhead=ListNode(0)
        while temp1 and temp2 :
            if temp1.val<=temp2.val :
                dummy.next=temp1
                temp1=temp1.next
            else :
                dummy.next=temp2
                temp2=temp2.next
            dummy=dummy.next
        dummy.next=temp1 if temp1 else temp2
        return dummyhead.next
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Find middle of LL create 2 LL head---mid and mid+1---None
        if not head or not head.next : return head
        slow, fast=head, head.next
        while fast and fast.next :
            slow=slow.next
            fast=fast.next.next
        temp=slow.next
        slow.next=None
        ll1=self.sortList(head)
        ll2=self.sortList(temp)
        #Do merge operation to sort the LL
        return self.merge(ll1,ll2)



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna