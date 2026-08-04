'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
	
class Solution:
    def segregate(self, head):
        #code here
        zerohead=zero=Node (-1)
        onehead=one=Node (-1)
        twohead=two=Node (-1)
        temp=head
        while temp :
            nxt=temp.next
            temp.next=None
            if temp.data==0 :
                zero.next=temp
                zero=zero.next
            elif temp.data==1 :
                one.next=temp
                one=one.next
            else :
                two.next=temp
                two=two.next
            temp=nxt
        #Point last LL's node to None 
        two.next=None
        if onehead.next : zero.next=onehead.next
        else : zero.next=twohead.next
        
        if twohead.next : one.next=twohead.next
        
        if zerohead.next : return zerohead.next 
        elif onehead.next : return onehead.next
        return twohead.next
        
    

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna