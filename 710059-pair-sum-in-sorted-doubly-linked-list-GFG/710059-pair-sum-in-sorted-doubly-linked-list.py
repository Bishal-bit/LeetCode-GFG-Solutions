# Structure of Doubly Linked List Node
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def findtail(self, temp) :
        while temp.next :
            temp=temp.next
        return temp
    def givenSumPairs(self, head, target):
        # code here
        temp1=head
        temp2=self.findtail(head)
        ans=[]
        while temp1.data < temp2.data :
            if temp1.data+temp2.data==target : 
                ans.append([temp1.data, temp2.data])
                temp1=temp1.next
                temp2=temp2.prev
            elif temp1.data+temp2.data> target : 
                temp2=temp2.prev
            else : temp1=temp1.next
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna