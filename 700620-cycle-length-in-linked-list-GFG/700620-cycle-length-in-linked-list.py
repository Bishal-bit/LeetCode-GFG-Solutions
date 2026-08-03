''' Structure of Linked List Node
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''
class Solution:
    def lengthOfLoop(self, head):
        #code here
        #Go similer to cycle detection algorithm of LL
        slow=fast=head
        while fast and fast.next :
            slow=slow.next
            fast=fast.next.next
            #If slow==fast i.e. cycle detected then break
            if slow==fast : break
        #Executes only if the while loop ends without a break
        else : return 0  
        #Initialize count as 1
        count=1
        #Declare temp as slow.next
        temp=slow.next
        #while temp!=slow increment count and update temp
        while temp!=slow :
            count+=1
            temp=temp.next
        #Return count
        return count
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna