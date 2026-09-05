# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: Optional[ListNode]) :
        #Reverse LL 
        temp=nex=head
        pre=None
        while temp :
            nex=temp.next
            temp.next=pre
            pre=temp
            temp=nex
        return pre
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next : return True
        #Go similer to cycle detection algorithm of LL to find the middle node
        slow=fast=head
        while fast and fast.next :
            slow=slow.next
            fast=fast.next.next
            #If slow==fast i.e. cycle detected then break
            if slow==fast : break
        #From middle node reverse the the rest of the LL
        temp1=self.reverse(slow)
        #Now compare from head untill middle and middle to end node to know if it is palindrome or not
        temp0=head
        while temp1 :
            if temp0.val!=temp1.val : return False
            temp0=temp0.next
            temp1=temp1.next
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna