''' Structure of Linked List Node
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''
class Solution:
    def lengthOfLoop(self, head):
        #code here
        slow=fast=head
        #Go similer to cycle detection algorithm of LL
        while fast and fast.next :
            slow=slow.next
            fast=fast.next.next
            #If slow==fast i.e. cycle detected then break
            if slow==fast : break
        #Else executes when the loop finishes normally i.e. it was not stopped by break
        else : return 0      #If there is no loop
        #Initialize temp as slow.next and count as 1
        temp=slow.next
        count=1   
        #Go untill temp becomes equal to slow and increment count
        while slow!=temp :
            temp=temp.next
            count+=1
        #Return count
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna